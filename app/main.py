# app/main.py
import os

from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr
from app import email_utils, models, database, schemas, tasks, utils

from sqlalchemy.orm import Session
from sqlalchemy import text

from jinja2 import Environment, FileSystemLoader

# 获取对应公司邮件模板
def render_invitation_template(buyer_name: str, project_name: str, template_name: str):

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(base_dir, "app/email_templates")

    if not os.path.exists(template_dir):
        return f"目录不存在: {template_dir}"

    # files = os.listdir(template_dir)
    # return [f for f in files if os.path.isfile(os.path.join(template_dir, f))]

    env = Environment(loader=FileSystemLoader(template_dir))

    template = env.get_template(template_name)
    return template.render(buyer_name=buyer_name, project_name=project_name)

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
    
    p_serial_number = next((s for s in req.serial_numbers if s.startswith("PR")), "")
    f_serial_number = next((s for s in req.serial_numbers if s.startswith("HK")), "")
    l_serial_number = next((s for s in req.serial_numbers if not (s.startswith("PR") or s.startswith("HK"))), "")

    project_info = models.ProjectInfo(
        project_name=req.project_name,
        contract_number="",
        tender_number=req.bidding_code, # 招标编号
        p_serial_number=p_serial_number,
        l_serial_number=l_serial_number,
        f_serial_number=f_serial_number,
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
        return {"message": "没有找到 D 类型的公司"}

    # B公司邮箱（可从数据库中查，也可固定写）
    b_company_info = (
        db.query(models.CompanyInfo)
        .filter(models.CompanyInfo.company_name == req.buyer_name)
        .first()
    )

    if not b_company_info:
        return {"message": "没有找到 B 类型的公司"}

    print("B公司信息：", b_company_info)
        
    # 给三家公司发送邮件
    for company in d_companies:

        print("D公司信息：", company.company_name, company.short_name)
        
        # 领先
        if company.short_name == "LF":
            subject = f" 《{ req.project_name }》- 投標委託 | 《{ b_company_info.company_name }》| 《25LDF_001》"
            print("LF公司邮件主题：", subject)
            template_name = "a1_lf.txt"

            smtp_config = {
                "host": "smtp.163.com",
                "port": 465,
                "username": "peterlcylove@163.com",
                "password": "ECRVsnXCe2g2Xauq",
                "from": "peterlcylove@163.com"
            }

            #TODO 每个公司有不同的发送模板 
            content = render_invitation_template(req.purchase_department, req.project_name, template_name)
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
            subject = f"【誠邀合作】《{ req.project_name }》投標《HK-FRONT-25#001》"
            print("FR公司邮件主题：", subject)
            template_name = "a1_fraun.txt"
            smtp_config = {
                "host": "smtp.163.com",
                "port": 465,
                "username": company.email,
                "password": "授权码",
                "from": company.email
            }
            
            content = render_invitation_template(req.purchase_department, req.project_name, template_name)
            print("FR公司邮件内容：", content)
            try:
                # email_utils.send_email(to_email=b_company_info.email, subject=subject, content=content, smtp_config=smtp_config)
                print("FR公司邮件发送成功")
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
            subject = f"《{ req.project_name }》投標委託《{ f_serial_number }》"
            print("普利赛斯公司邮件主题：", subject)
            template_name = "a1_precise.txt"
            smtp_config = {
                "host": "smtp.163.com",
                "port": 465,
                "username": company.email,
                "password": "D8VsKe73at2pC2LQ",
                "from": company.email
            }
            
            content = render_invitation_template(req.purchase_department, req.project_name, template_name)
            print("普利赛斯公司邮件内容：", content)
            success, error = await email_utils.send_email(to=company.email, subject=subject, body=content, smtp_config=smtp_config)
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

    #TODO 定时任务：5-60分钟后由 B公司 给3家公司回复邮件
    random_numbers = utils.generate_random_number()

    # 假设 B 公司固定使用以下邮箱配置（也可以从 DB 查）
    b_company_smtp = {
        "host": "smtp.163.com",
        "port": 465,
        "username": b_company_info.email,
        "password": "授权码",
        "from": b_company_info.email
    }

    # JZ 测试，后替换为实际的B公司
    if company.short_name == "JZ":
        subject = f"《{req.project_name}》《{l_serial_number}》"
        template_name = "a2_jz_reply.txt"
        content = render_invitation_template(req.purchase_department, req.project_name, template_name)
        for company in d_companies:
            result = tasks.send_reply_email.apply_async(
                args=[company.email, subject, content, b_company_smtp],
                countdown=random_numbers.pop(0) * 60  # 延迟 5 分钟（单位：秒）
            )
            # 保存发送记录
            record = models.EmailRecord(
                to=company.email,
                subject=subject,
                body=content,
                status="pending", 
                task_id=result.task_id
            )
            db.add(record)
            db.commit()
            db.refresh(record)


    return {"message": "邮件已成功发送给 B 公司"}


"""
合同审批流程通过后，确认是否要发送邮件
发送条件：
    1. 带有L流水号，P流水号，F流水号

这个函数要做的事情：
    1. 
"""
def after_contract_audit():