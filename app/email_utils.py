# app/email_utils.py
import os
import random 

from aiosmtplib import SMTP
from email.message import EmailMessage
# from app.tasks import send_reply_email
from app import database, models

from jinja2 import Environment, FileSystemLoader, select_autoescape
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from contextlib import contextmanager

@contextmanager
def get_db_session():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def send_email(to: str, subject: str, body: str, smtp_config: dict):
    message = EmailMessage()
    message["From"] = smtp_config["from"]
    message["To"] = to
    message["Subject"] = subject
    # 设置 HTML 正文
    message.add_alternative(body, subtype="html")

    try:
        smtp = SMTP(hostname=smtp_config["host"], port=smtp_config["port"], use_tls=True)
        await smtp.connect()
        await smtp.login(smtp_config["username"], smtp_config["password"])
        await smtp.send_message(message)
        await smtp.quit()
        return True, ""
    except Exception as e:
        return False, str(e)


# 获取对应公司邮件发送标题
# 1. 邮件阶段
# 2. 公司简称
# 3. 项目名称
# 4. 对应公司流水号
def render_email_subject(stage: str, company_short_name: str, project_name: str, serial_number: str) -> str:
    # 从数据库中获取标题模板
    
    with get_db_session() as db:
        subject = db.query(models.EmailSubject).filter(
            models.EmailSubject.stage == stage,
            models.EmailSubject.short_name == company_short_name,
            # models.EmailSubject.project_name == project_name,
        ).first()

        if not subject:
            return f"{stage}_{company_short_name}_{project_name}"
        
        return subject.subject.format(
            company_name=subject.company_name,
            short_name=subject.short_name,
            project_name=project_name,
            serial_number=serial_number
        )

# 获取对应公司邮件模板并渲染内容
def render_invitation_template_content(buyer_name: str, project_name: str, template_name: str):
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(base_dir, "app", "email_templates")

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'xml'])  # 自动转义 HTML
    )

    template = env.get_template(template_name)  # 例如 "bidding_invite.html"
    return template.render(buyer_name=buyer_name, project_name=project_name)




