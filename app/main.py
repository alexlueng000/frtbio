# app/main.py
from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr
from . import email_utils, models, database
from sqlalchemy.orm import Session

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


'''
委托投标
第一封邮件：三家D公司给B公司发送邮件    
'''
@app.post("/send_email")
async def recieve_bidding_register(req: schemas.SendEmailRequest, db: Session = Depends(database.get_db)):
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
    b_company_email = "b_company@example.com"

    for company in d_companies:
        subject = f"关于项目 {req.project_name} 的合作信息"
        content = (
            f"尊敬的 B 公司：\n\n"
            f"我们是 {company.company_name}。\n"
            f"现将关于如下项目的信息发送给您：\n"
            f"采购单位：{req.buyer_name}\n"
            f"项目名称：{req.project_name}\n"
            f"流水号：{req.serial_number}\n\n"
            f"感谢您的关注。\n\n"
            f"此致\n{company.company_name}"
        )
        send_email(to_email=b_company_email, subject=subject, content=content)

    return {"message": "邮件已成功发送给 B 公司"}