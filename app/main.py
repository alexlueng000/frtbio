# app/main.py
from pathlib import Path
from datetime import datetime
from decimal import Decimal
import logging

from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from sqlalchemy import text

from app import email_utils, models, database, schemas, tasks, send_email_tasks

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger(__name__)

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

# 将 ~/settlements 目录挂载为 /download 路由
settlement_dir = Path.home() / "settlements"
app.mount("/download", StaticFiles(directory=settlement_dir), name="download")


@app.get("/ping-db")
def ping_db():
    try:
        with database.engine.connect() as conn:
            conn.execute(text("SELECT 1")) 
        return {"status": "success", "message": "pong ✅ 数据库连接成功"}
    except Exception as e:
        return {"status": "error", "message": "❌ 数据库连接失败", "detail": str(e)}

'''
1. 委托投标
第一封邮件：三家D公司给B公司发送邮件    
接收流水号：['PR202504001', '25LDF_001', 'HK-FRONT-25#001']
'''

"""
这个接口需要处理的事情：
1. 向project_info表中插入一条项目信息
2. 查询3家D公司的信息
3. 查询B公司的信息（如果没有呢？）
4. 3家D公司给B公司发送邮件
5. 保存发送记录，处理异常情况并更新project_info中的A1字段
6. 生成一个5-60之间的随机数x，在x分钟后由B向3个D公司发送A2邮件
7. 保存发送记录，处理异常情况并更新project_info中的A2字段
8. 将发送记录回传给宜搭 TODO

接收参数：
@serials_numbers: 流水号列表，例如 ['PR202504001', '25LDF_001', 'HK-FRONT-25#001'] （必有）
@purchase_department: 采购单位 （必有）
@b_company_name: B公司名称 （必有）
@project_name: 项目名称 （必有）
@bidding_code: 招标编号 （可能为空）
"""
@app.post("/receive_bidding_register")
async def receive_bidding_register(req: schemas.BiddingRegisterRequest, db: Session = Depends(database.get_db)):

    logger.info("1委托投标登记|请求参数：%s", req.model_dump())

    # 新增一条项目信息
    project_info = models.ProjectInfo(
        project_name=req.project_name,
        contract_number="",
        tender_number=req.bidding_code, # 招标编号
        project_type="",
        # project_stage="A",
        p_serial_number=req.p_serial_number,
        l_serial_number=req.l_serial_number,
        f_serial_number=req.f_serial_number,
        purchaser=req.purchase_department,
        company_b_name=req.b_company_name,
        company_c_name="",
        company_d_name="",
        a1=False,
        a2=False,
        b3=False,
        b4=False,
        b5=False, 
        b6=False,
        c7=False,
        c8=False,
        c9=False,
        c10=False
    )
    db.add(project_info)
    db.commit()
    db.refresh(project_info) # 获取插入后的主键ID

    # 获取插入后的主键ID, 用于后续邮件记录
    project_id = project_info.id

    # 查询三家D公司
    d_companies = (
        db.query(models.CompanyInfo)
        .filter(models.CompanyInfo.company_type == "D")
        .limit(3)
        .all()
    )

    if not d_companies:
        # TODO 回传错误信息到宜搭
        logger.error("没有找到 D 类型的公司")
        return {"message": "没有找到 D 类型的公司"}

    # B公司邮箱（可从数据库中查，也可固定写）

    logger.info("B公司名称：", req.b_company_name)
    b_company_info = (
        db.query(models.CompanyInfo)
        .filter(models.CompanyInfo.company_name == req.b_company_name)
        .first()
    )

    if not b_company_info:
        # TODO 回传错误信息到宜搭
        logger.error("没有找到 B 公司")
        return {"message": "没有找到 B 公司"}

    logger.info("B公司信息：", b_company_info)
        
    # 三家D公司给B公司发送A1邮件
    for company in d_companies:

        # print("D公司信息：", company.company_name, company.short_name)
        
        # 领先
        if company.short_name == "LF":
            subject = f" { req.project_name }- 投標委託 | { b_company_info.company_name }| { req.l_serial_number }"
            # print("LF公司邮件主题：", subject)
            template_name = "A1_LF.html"

            smtp_config = {
                "host": "smtp.163.com",
                "port": 465,
                "username": "peterlcylove@163.com",
                "password": "ECRVsnXCe2g2Xauq",
                "from": "peterlcylove@163.com"
            }

            #TODO 每个公司有不同的发送模板 
            content = email_utils.render_invitation_template_content(
                buyer_name=req.purchase_department,
                project_name=req.project_name,
                template_name=template_name
            )
            # print("LF公司邮件内容：", content)  
            success, error = email_utils.send_email_in_main(to=b_company_info.email, subject=subject, body=content, smtp_config=smtp_config)
            
            # 保存发送记录
            record = models.EmailRecord(
                to=b_company_info.email,
                subject=subject,
                body=content,
                status="success" if success else "failed",
                error_message=error if not success else None,
                project_id=project_id,
                task_id="",
                stage="A1",
                actual_sending_time=datetime.now()
            )
            db.add(record)
            db.commit()
            db.refresh(record)
            
        # 弗劳恩
        elif company.short_name == "FR":
            subject = f"【誠邀合作】{ req.project_name }投標{req.f_serial_number}"
            print("FR公司邮件主题：", subject)
            template_name = "A1_FR.html"
            smtp_config = {
                "host": "smtp.163.com",
                "port": 465,
                "username": "peterlcylove@163.com",
                "password": "ECRVsnXCe2g2Xauq",
                "from": "peterlcylove@163.com"
            }
            
            content = email_utils.render_invitation_template_content(
                buyer_name=req.purchase_department,
                project_name=req.project_name,
                template_name=template_name
            )
            # print("FR公司邮件内容：", content)
            try:
                # email_utils.send_email(to_email=b_company_info.email, subject=subject, content=content, smtp_config=smtp_config)
                # print("FR公司邮件发送成功")
                success, error = email_utils.send_email_in_main(to=b_company_info.email, subject=subject, body=content, smtp_config=smtp_config)

            except Exception as e:
                print("FR公司邮件发送失败：", e)
            # email_utils.send_email(to_email=b_company_info.email, subject=subject, content=content, smtp_config=smtp_config)
            # 保存发送记录
            record = models.EmailRecord(
                to=b_company_info.email,
                subject=subject,
                body=content,
                status="success" if success else "failed",
                error_message=error if not success else None,
                project_id=project_id,
                stage="A1",
                actual_sending_time=datetime.now()
            )
            db.add(record)
            db.commit()
            db.refresh(record)
        # 普利赛斯
        else:
            subject = f"{ req.project_name }投標委託{ req.p_serial_number }"
            print("普利赛斯公司邮件主题：", subject)
            template_name = "A1_PRESICE.html"
            smtp_config = {
                "host": "smtp.163.com",
                "port": 465,
                "username": "peterlcylove@163.com",
                "password": "ECRVsnXCe2g2Xauq",
                "from": "peterlcylove@163.com"
            }
            
            content = email_utils.render_invitation_template_content(
                buyer_name=req.purchase_department,
                project_name=req.project_name,
                template_name=template_name
            )
            # print("普利赛斯公司邮件内容：", content)
            success, error = email_utils.send_email_in_main(to=company.email, subject=subject, body=content, smtp_config=smtp_config)
            # 保存发送记录
            record = models.EmailRecord(
                to=company.email,
                subject=subject,
                # body=content,
                status="success" if success else "failed",
                error_message=error if not success else None,
                task_id="",
                project_id=project_id,
                stage="A1",
                actual_sending_time=datetime.now()
            )
            db.add(record)
            db.commit()
            db.refresh(record)

    #TODO 定时任务：5-60分钟后由 B公司 给3家公司回复邮件
    # random_numbers = utils.generate_random_number()

    # # 假设 B 公司固定使用以下邮箱配置（也可以从 DB 查）
    # b_company_smtp = {
    #     "host": "smtp.163.com",
    #     "port": 465,
    #     "username": "peterlcylove@163.com",
    #     "password": "ECRVsnXCe2g2Xauq",
    #     "from": "peterlcylove@163.com"
    # }

    d_smtp = {
        "host": "smtp.qq.com",
        "port": 465,
        "username": "494762262@qq.com",
        "password": "mlnbblbyyvulbhhi",
        "from": "494762262@qq.com"
    }

   
    
    template_name = "A2_" + b_company_info.short_name + ".html"

    # # JZ 测试，后替换为实际的B公司
    for company in d_companies:

        A2_subject = ''

        if company.short_name == "FR":

            A2_subject = email_utils.render_email_subject(
                stage="A2", 
                company_short_name=b_company_info.short_name, 
                project_name=req.project_name,
                serial_number=req.f_serial_number
            )
            print("FR公司邮件主题：", A2_subject)
            
        elif company.short_name == "LF":
            A2_subject = email_utils.render_email_subject(
                stage="A2", 
                company_short_name=b_company_info.short_name, 
                project_name=req.project_name,
                serial_number=req.l_serial_number
            )
            print("LF公司邮件主题：", A2_subject)
            
        
        else:
            A2_subject = email_utils.render_email_subject(
                stage="A2", 
                company_short_name=b_company_info.short_name, 
                project_name=req.project_name,
                serial_number=req.p_serial_number
            )
            print("Precise公司邮件主题：", A2_subject)
            
        
        
        content = email_utils.render_invitation_template_content(
            # purchase_department=req.purchase_department,
            project_name=req.project_name,
            template_name=template_name,
            full_name=company.contact_person,
        )
            
        result = tasks.send_reply_email.apply_async(
            args=[company.email, A2_subject, content, d_smtp, 1 * 60, "A2", project_id],
            countdown=1 * 60  
        )
        # 保存发送记录
        record = models.EmailRecord(
            to=company.email,
            subject=A2_subject,
            body=content,
            status="pending", 
            task_id=result.task_id,
            project_id=project_id,
            stage="A2"
        )
        db.add(record)
        db.commit()
        db.refresh(record)

    # 更新project_info表中的a1状态为1
    project_info.a1 = True
    db.commit()
            
    return {"message": "邮件已成功发送给 B 公司"}



# === 项目中标信息 ===
# 更新项目中标信息的合同号，招标编号
# 接收参数：
#     1. 项目名称
#     2. L流水号，P流水号，F流水号
#     3. 招标编号
#     4. 合同号
@app.post("/project_bidding_winning_information")
async def project_bidding_winning_information(req: schemas.ProjectWinningInfoRequest, db: Session = Depends(database.get_db)):

    logger.info("2项目中标信息|请求参数：%s", req.model_dump())
    
    project_information = db.query(models.ProjectInfo).filter_by(p_serial_number=req.p_serial_number, l_serial_number=req.l_serial_number, f_serial_number=req.f_serial_number).first()
    
    if not project_information:
        logger.error("2项目中标信息|没有找到项目信息，流水号为：", req.l_serial_number, req.p_serial_number, req.f_serial_number)
        return {"message": "没有找到项目信息"}

    project_information.contract_number = req.contract_number
    project_information.tender_number = req.bidding_code

    # 3. 尝试将中标金额转换为 Decimal
    try:
        winning_amount = Decimal(req.winning_amount)
    except:
        raise HTTPException(status_code=400, detail="中标金额格式错误，应为数字")
    
    # 5. 创建并插入中标费用详情记录
    fee_detail = models.ProjectFeeDetails(
        project_id=project_information.id,
        winning_time=req.winning_time,
        winning_amount=winning_amount
    )
    db.add(fee_detail)
    db.commit()
    db.refresh(fee_detail)
    
    return {"message": "项目中标信息更新成功"}



"""
合同审批流程通过后，确认是否要发送邮件
发送条件：
    1. 带有L流水号，P流水号，F流水号

这个函数要做的事情：
    1. 判断是否首次调用这个接口（D公司修改后会重新触发）
    2. 判断项目类型：BCD, CCD, BC, BD
    3. 发送邮件
    4. 保存发送记录
    5. 返回信息给宜搭

这个接口接收的参数：
    1. 项目名称
    2. L流水号，P流水号，F流水号
    3. 合同号
    4. 合同流水号
    5. B公司-中标商
    6. C公司 C=列表-合同类型（货款收付控制---不含供应商两方采购合同）中，合同类型=三方/四方合同，且收付控制=付的付款方
    7. D公司 D=列表-合同类型（货款收付控制---不含供应商两方采购合同）中，合同类型=三方/四方合同，且收付控制=付的付款方
    8. 合同类型 contract_type
"""
@app.post("/contract_audit")
async def contract_audit(req: schemas.ContractAuditRequest, db: Session = Depends(database.get_db)):

    logger.info("3合同审核|请求参数: %s", req.model_dump())
    
    # 🔍 判断是否包含“三方/四方合同”
    has_target_contract_type = any(
        contract.selectField_l7ps2ca3 == "三方/四方合同" for contract in req.contracts
    )

    if not has_target_contract_type:
        logger.info("没有找到三方/四方合同，不发送邮件")
        return {"message": "没有找到三方/四方合同，不发送邮件"}
    
    # 如果没有L流水号，P流水号，F流水号，说明不是委托投标登记项目，不发送邮件
    if not req.l_serial_number or not req.p_serial_number or not req.f_serial_number:
        logger.info("没有L流水号，P流水号，F流水号，不发送邮件")
        return {"message": "没有L流水号，P流水号，F流水号，不发送邮件"}

    # 项目类型
    project_type = ''

    # TODO 判断是否首次调用这个接口, 需要根据合同号来判断
    project = db.query(models.ProjectInfo).filter(models.ProjectInfo.project_name == req.project_name).first()
    if not project:
        logger.info("没有找到项目信息，不发送邮件")
        return {"message": "没有找到项目信息，不发送邮件"}
    if not project.project_type != '': # 说明之前已经判断过了项目类型，是D公司信息有修改的情况
        pass
    
    
    # C公司名字是 selectField_l7ps2ca6 的值
    c_company_name = req.contracts[0].selectField_l7ps2ca6
    # D公司名字是 selectField_l7ps2ca7 的值
    d_company_name = req.contracts[0].selectField_l7ps2ca7

    # 确定B、C、D公司是否内部公司，B、D公司是内部公司才发送邮件
    b_company = db.query(models.CompanyInfo).filter(
        models.CompanyInfo.company_name == req.company_b_name, models.CompanyInfo.company_type == 'B'
    ).first()
    # 如果找到了B公司，说明是内部公司
    if not b_company:
        return {"message": "没有找到B公司，不发送邮件"}
    d_company = db.query(models.CompanyInfo).filter(models.CompanyInfo.company_name == d_company_name, models.CompanyInfo.company_type == 'D').first()
    # 如果找到了D公司，说明是内部公司
    if not d_company:
        return {"message": "没有找到D公司，不发送邮件"}

    c_company = db.query(models.CompanyInfo).filter(models.CompanyInfo.company_name == c_company_name, models.CompanyInfo.company_type == 'C').first()
    # 如果找到了C公司，说明是内部公司，如果没有找到，说明是外部公司
    if not c_company:
        project_type = 'BD'
    # 如果B公司和C公司是同一家公司，说明是CCD项目
    elif b_company.company_name == c_company.company_name:
        project_type = 'CCD'
    else:
        project_type = 'BCD'

    # 更新project_info表中的项目类型
    project = db.query(models.ProjectInfo).filter(models.ProjectInfo.contract_number == req.contract_number).first()
    if project:
        project.project_type = project_type
        db.add(project)
        db.commit()
        db.refresh(project)

    # 发送邮件

    # BCD 类型项目
    if project_type == 'BCD':
        send_email_tasks.schedule_bid_conversation_BCD(
            b_company=b_company,
            c_company=c_company,
            d_company=d_company,
            contract_serial_number=req.contract_serial_number,
            project_name=req.project_name,
            winning_amount=req.winning_amount,
            winning_time=req.winning_time,
            contract_number=req.contract_number
        )
    # CCD 类型项目
    elif project_type == 'CCD':
        send_email_tasks.schedule_bid_conversation_CCD(b_company, c_company, d_company)
    # BD 类型项目
    else:
        send_email_tasks.schedule_bid_conversation_BD(b_company, d_company)
    
    logger.info("合同审批阶段邮件已成功发送，合同号为%s", req.contract_number)


    #TODO 返回邮件实际发送时间
    return {
        "message": f"合同审批阶段邮件已成功发送，合同号为{req.contract_number}",
        "project_type": project_type
    }
    
    
    

# 结算流程后发送邮件
# 顺序：
# 1. 发送C-B间结算单
# 2. 发送B-D间结算单
# 3. B-D间结算单确认
# 4. C-D间结算单确认

# @参数
# project_type: str, 项目类型
# project_name: str, 项目名称
# l_serial_number: str, L流水号
# p_serial_number: str, P流水号
# f_serial_number: str, F流水号
# contract_number: str, 合同号
# b_company_name: str, B公司名称
# c_company_name: str, C公司名称
# d_company_name: str, D公司名称
# 还有很多金额

@app.post("/settlement")
def settlement(
    req: schemas.SettlementRequest, db: Session = Depends(database.get_db)):

    logger.info("4结算|请求参数：%s", req.model_dump())

    project_information = db.query(models.ProjectInfo).filter_by(contract_number=req.contract_number).first()
    if not project_information:
        logger.info("没有找到项目信息，不发送邮件，合同号为: %s", req.contract_number)
        return {"message": "没有找到项目信息"}

    winning_time = "2025-06-15"
    #TODO 更新project_fee_details表
    

    b_company = db.query(models.CompanyInfo).filter_by(company_name=project_information.company_b_name).first()
    if not b_company:
        logger.info("没有找到B公司，不发送邮件，合同号为: %s", req.contract_number)
        return {"message": "没有找到B公司"}

    d_company = db.query(models.CompanyInfo).filter_by(company_name=project_information.company_d_name).first()
    if not d_company:
        logger.info("没有找到D公司，不发送邮件，合同号为: %s", req.contract_number)
        return {"message": "没有找到D公司"}

    c_company = db.query(models.CompanyInfo).filter_by(company_name=project_information.company_c_name).first()
    if not c_company:
        logger.info("没有找到C公司，不发送邮件，合同号为: %s", req.contract_number)
        # 说明是BD项目
        pass 

    BC_download_url = ""
    BD_download_url = ""

    if project_information.project_type == 'BCD':
        result = send_email_tasks.schedule_settlement_BCD(
            b_company=b_company,
            c_company=c_company,
            d_company=d_company,
            contract_number=project_information.contract_number,
            contract_serial_number=req.contract_serial_number,
            project_name=req.project_name,
            amount=req.amount,
            three_fourth=req.three_fourth,
            import_service_fee=req.import_service_fee,
            third_party_fee=req.third_party_fee,
            service_fee=req.service_fee,
            win_bidding_fee=req.win_bidding_fee,
            bidding_document_fee=req.bidding_document_fee,
            bidding_service_fee=req.bidding_service_fee,
            winning_time=winning_time
        )
        BC_download_url = result["BC_download_url"]
        BD_download_url = result["BD_download_url"]
    else:
        result = send_email_tasks.schedule_settlement_CCD_BD(
            b_company=b_company,
            c_company=c_company,
            d_company=d_company,
            contract_number=project_information.contract_number,
            contract_serial_number=req.contract_serial_number,
            project_name=req.project_name,
            amount=req.amount,
            three_fourth=req.three_fourth,
            import_service_fee=req.import_service_fee,
            third_party_fee=req.third_party_fee,
            service_fee=req.service_fee,
            win_bidding_fee=req.win_bidding_fee,
            bidding_document_fee=req.bidding_document_fee,
            bidding_service_fee=req.bidding_service_fee,
            winning_time=winning_time
        )
        # BC_download_url = result["BC_download_url"]
        BD_download_url = result["BD_download_url"]

    logger.info("BC_download_url: %s, BD_download_url: %s", BC_download_url, BD_download_url)

    return {
        "message": f"结算邮件已成功发送，合同号为{req.contract_number}",
        "BC_download_url": BC_download_url,
        "BD_download_url": BD_download_url
    }
