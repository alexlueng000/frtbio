# app/main.py
from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr
from app import email_utils, models, database, schemas, tasks, utils

from sqlalchemy.orm import Session
from sqlalchemy import text


app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

class EmailSchema(BaseModel):
    to: EmailStr
    subject: str
    body: str

@app.post("/send-email")
async def send(email: EmailSchema, db: Session = Depends(database.get_db)):
    smtp_config = {
        "host": "smtp.163.com",
        "port": 465,
        "username": "你的邮箱",
        "password": "授权码",
        "from": "你的邮箱"
    }

    success, error = await email_utils.send_email(email.to, email.subject, email.body, smtp_config)
    
    # 保存发送记录
    record = models.EmailRecord(
        to=email.to,
        subject=email.subject,
        body=email.body,
        status="success" if success else "failed",
        error_message=error if not success else None
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return {"success": success, "error": error}


@app.get("/ping-db")
def ping_db():
    try:
        with database.engine.connect() as conn:
            conn.execute(text("SELECT 1")) 
        return {"status": "success", "message": "pong ✅ 数据库连接成功"}
    except Exception as e:
        return {"status": "error", "message": "❌ 数据库连接失败", "detail": str(e)}


email_templates_name = {
    "a1_ld": "a1_ld.txt",
    "a1_fraun": "a1_fraun.txt"
}

'''
1. 委托投标
第一封邮件：三家D公司给B公司发送邮件    
接收流水号：['PR202504001', '25LDF_001', 'HK-FRONT-25#001']
'''

@app.post("/test_recieve_bidding_register")
async def test_recieve_bidding_register(req: schemas.BiddingRegisterRequest, db: Session = Depends(database.get_db)):
    
    # 查询三家D公司
    d_companies = (
        db.query(models.CompanyInfo)
        .filter(models.CompanyInfo.company_type == "D")
        .limit(3)
        .all()
    )

    if not d_companies:
        return {"message": "没有找到 D 类型的公司"}

    return {"d_companies": [company.company_name for company in d_companies]}


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
@app.post("/recieve_bidding_register")
async def recieve_bidding_register(req: schemas.BiddingRegisterRequest, db: Session = Depends(database.get_db)):

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

    # 查询三家D公司
    d_companies = (
        db.query(models.CompanyInfo)
        .filter(models.CompanyInfo.company_type == "D")
        .limit(3)
        .all()
    )

    if not d_companies:
        # TODO 回传错误信息到宜搭
        return {"message": "没有找到 D 类型的公司"}

    # B公司邮箱（可从数据库中查，也可固定写）

    print("B公司名称：", req.b_company_name)
    b_company_info = (
        db.query(models.CompanyInfo)
        .filter(models.CompanyInfo.company_name == req.b_company_name)
        .first()
    )

    if not b_company_info:
        # TODO 回传错误信息到宜搭
        return {"message": "没有找到 B 公司"}

    print("B公司信息：", b_company_info)
        
    # 三家D公司给B公司发送A1邮件
    for company in d_companies:

        # print("D公司信息：", company.company_name, company.short_name)
        
        # 领先
        if company.short_name == "LF":
            subject = f" { req.project_name }- 投標委託 | { b_company_info.company_name }| { req.f_serial_number }"
            # print("LF公司邮件主题：", subject)
            template_name = "a1_lf.txt"

            smtp_config = {
                "host": "smtp.163.com",
                "port": 465,
                "username": "peterlcylove@163.com",
                "password": "ECRVsnXCe2g2Xauq",
                "from": "peterlcylove@163.com"
            }

            #TODO 每个公司有不同的发送模板 
            content = email_utils.render_invitation_template_content(req.purchase_department, req.project_name, template_name)
            print("LF公司邮件内容：", content)  
            success, error = await email_utils.send_email(to=b_company_info.email, subject=subject, body=content, smtp_config=smtp_config)
            
            # 保存发送记录
            record = models.EmailRecord(
                to=b_company_info.email,
                subject=subject,
                body=content,
                status="success" if success else "failed",
                error_message=error if not success else None
            )
            db.add(record)
            db.commit()
            db.refresh(record)
            
        # 弗劳恩
        elif company.short_name == "FR":
            subject = f"【誠邀合作】{ req.project_name }投標{req.f_serial_number}"
            print("FR公司邮件主题：", subject)
            template_name = "A1_FRAUN.html"
            smtp_config = {
                "host": "smtp.163.com",
                "port": 465,
               "username": "peterlcylove@163.com",
                "password": "ECRVsnXCe2g2Xauq",
                "from": "peterlcylove@163.com"
            }
            
            content = email_utils.render_invitation_template_content(req.purchase_department, req.project_name, template_name)
            print("FR公司邮件内容：", content)
            try:
                # email_utils.send_email(to_email=b_company_info.email, subject=subject, content=content, smtp_config=smtp_config)
                # print("FR公司邮件发送成功")
                success, error = await email_utils.send_email(to=b_company_info.email, subject=subject, body=content, smtp_config=smtp_config)

            except Exception as e:
                print("FR公司邮件发送失败：", e)
            # email_utils.send_email(to_email=b_company_info.email, subject=subject, content=content, smtp_config=smtp_config)
            # 保存发送记录
            record = models.EmailRecord(
                to=b_company_info.email,
                subject=subject,
                body=content,
                status="success" if success else "failed",
                error_message=error if not success else None
            )
            db.add(record)
            db.commit()
            db.refresh(record)

        # 普利赛斯
        else:
            subject = f"{ req.project_name }投標委託{ req.f_serial_number }"
            print("普利赛斯公司邮件主题：", subject)
            template_name = "A1_PRESICE.html"
            smtp_config = {
                "host": "smtp.163.com",
                "port": 465,
                "username": "peterlcylove@163.com",
                "password": "ECRVsnXCe2g2Xauq",
                "from": "peterlcylove@163.com"
            }
            
            content = email_utils.render_invitation_template_content(req.purchase_department, req.project_name, template_name)
            # print("普利赛斯公司邮件内容：", content)
            success, error = await email_utils.send_email(to=company.email, subject=subject, body=content, smtp_config=smtp_config)
            # 保存发送记录
            record = models.EmailRecord(
                to=company.email,
                subject=subject,
                # body=content,
                status="success" if success else "failed",
                error_message=error if not success else None,
                task_id="",
            )
            db.add(record)
            db.commit()
            db.refresh(record)

    #TODO 定时任务：5-60分钟后由 B公司 给3家公司回复邮件
    # random_numbers = utils.generate_random_number()

    # # 假设 B 公司固定使用以下邮箱配置（也可以从 DB 查）
    b_company_smtp = {
        "host": "smtp.163.com",
        "port": 465,
        "username": "peterlcylove@163.com",
        "password": "ECRVsnXCe2g2Xauq",
        "from": "peterlcylove@163.com"
    }

    # # JZ 测试，后替换为实际的B公司
    if b_company_info.short_name == "DG":
        subject = f"{req.project_name} {req.l_serial_number}"
        template_name = "A2_DG.html"
        content = email_utils.render_invitation_template_content(req.purchase_department, req.project_name, template_name)
        
        result = tasks.send_reply_email.apply_async(
                args=["494762262@qq.com", subject, content, b_company_smtp],
                countdown=1 * 60  
            )
            # 保存发送记录
        record = models.EmailRecord(
            to="494762262@qq.com",
            subject=subject,
            body=content,
            status="pending", 
            task_id=result.task_id
        )
        db.add(record)
        db.commit()
        db.refresh(record)
            


    return {"message": "邮件已成功发送给 B 公司"}


# === 项目中标信息 ===
# 更新项目中标信息的合同号，招标编号
# 接收参数：
#     1. 项目名称
#     2. L流水号，P流水号，F流水号
#     3. 招标编号
#     4. 合同号

@app.post("/project_bidding_winning_information")
def project_bidding_winning_information():
    pass


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
    4. B公司-中标商
    5. C公司 C=列表-合同类型（货款收付控制---不含供应商两方采购合同）中，合同类型=三方/四方合同，且收付控制=付的付款方
    6. D公司 D=列表-合同类型（货款收付控制---不含供应商两方采购合同）中，合同类型=三方/四方合同，且收付控制=付的付款方
    7. 合同类型
"""
@app.post("/contract_audit")
def contract_audit():
    
    # 如果合同类型不是三方/四方合同，不发送邮件
    if contract_type != "三方/四方合同":
        return {"message": "合同类型不是三方/四方合同，不发送邮件"}
    
    # 如果没有L流水号，P流水号，F流水号，说明不是委托投标登记项目，不发送邮件
    if not l_serial_number or not p_serial_number or not f_serial_number:
        return {"message": "没有L流水号，P流水号，F流水号，不发送邮件"}

    # 判断项目类型
    project_type = ''

    # 判断是否首次调用这个接口
    project = db.query(models.ProjectInfo).filter(models.ProjectInfo.project_name == req.project_name).first()
    if not project.project_type != '': # 说明之前已经判断过了项目类型，是D公司信息有修改的情况
        pass
    

    # 确定B、C、D公司是否内部公司，B、D公司是内部公司才发送邮件
    b_company = db.query(models.CompanyInfo).filter(models.CompanyInfo.company_name == req.company_b_name, models.CompanyInfo.company_type == 'B').first()
    # 如果找到了B公司，说明是内部公司
    if not b_company:
        return {"message": "没有找到B公司，不发送邮件"}
    d_company = db.query(models.CompanyInfo).filter(models.CompanyInfo.company_name == req.company_d_name, models.CompanyInfo.company_type == 'D').first()
    # 如果找到了D公司，说明是内部公司
    if not d_company:
        return {"message": "没有找到D公司，不发送邮件"}

    c_company = db.query(models.CompanyInfo).filter(models.CompanyInfo.company_name == req.company_c_name, models.CompanyInfo.company_type == 'C').first()
    # 如果找到了C公司，说明是内部公司，如果没有找到，说明是外部公司
    if not c_company:
        project_type = 'BD'
    # 如果B公司和D公司是同一家公司，说明是CCD项目
    elif b_company.company_name == d_company.company_name:
        project_type = 'CCD'
    else:
        project_type = 'BCD'

    # 更新project_info表中的项目类型
    project = db.query(models.ProjectInfo).filter(models.ProjectInfo.project_name == req.project_name).first()
    if project:
        project.project_type = project_type
        db.add(project)
        db.commit()
        db.refresh(project)

    # 发送邮件

    # BCD 类型项目
    if project_type == 'BCD':
        email_utils.schedule_bid_conversation_BCD(b_company_name, c_company_name, d_company_name)
    # CCD 类型项目
    elif project_type == 'CCD':
        email_utils.schedule_bid_conversation_CCD(b_company_name, c_company_name, d_company_name)
    # BD 类型项目
    else:
        email_utils.schedule_bid_conversation_BD(b_company_name, d_company_name)
    
    return {"message": "邮件已成功发送"}
    
    
    

# 结算流程后发送邮件
# 顺序：
# 1. 发送C-B间结算单
# 2. 发送B-D间结算单
# 3. B-D间结算单确认
# 4. C-D间结算单确认
@app.post("/settlement")
def settlement(project_type: str, project_name: str, l_serial_number: str, p_serial_number: str, f_serial_number: str, contract_number: str, b_company_name: str, c_company_name: str, d_company_name: str):
    if project_type == 'BCD':
        email_utils.schedule_settlement_BCD(b_company_name, c_company_name, d_company_name)
    elif project_type == 'CCD':
        email_utils.schedule_settlement_CCD(b_company_name, c_company_name, d_company_name)
    elif project_type == 'BD':
        email_utils.schedule_settlement_BD(b_company_name, d_company_name)
    return {"message": "邮件已成功发送"}
