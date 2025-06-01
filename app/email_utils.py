# app/email_utils.py
import os
import random 

from aiosmtplib import SMTP
from email.message import EmailMessage
from app.tasks import send_reply_email

from jinja2 import Environment, FileSystemLoader

async def send_email(to: str, subject: str, body: str, smtp_config: dict):
    message = EmailMessage()
    message["From"] = smtp_config["from"]
    message["To"] = to
    message["Subject"] = subject
    message.set_content(body)

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
    db = database.get_db()
    return f"{stage} {company_short_name} {project_name} {serial_number}"


# 获取对应公司邮件模板并渲染内容
def render_invitation_template_content(buyer_name: str, project_name: str, template_name: str):

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(base_dir, "app/email_templates")

    if not os.path.exists(template_dir):
        return f"目录不存在: {template_dir}"

    # files = os.listdir(template_dir)
    # return [f for f in files if os.path.isfile(os.path.join(template_dir, f))]

    env = Environment(loader=FileSystemLoader(template_dir))

    template = env.get_template(template_name)
    return template.render(buyer_name=buyer_name, project_name=project_name)




# BCD 项目类型发送邮件
def schedule_bid_conversation_BCD(b_company_name: str, c_company_name: str, d_company_name: str):
    
    # 获取BCD三家公司的信息
    b_company = db.query(models.CompanyInfo).filter(models.CompanyInfo.company_name == b_company_name).first()
    c_company = db.query(models.CompanyInfo).filter(models.CompanyInfo.company_name == c_company_name).first()
    d_company = db.query(models.CompanyInfo).filter(models.CompanyInfo.company_name == d_company_name).first()

    b_smtp = {
        "host": b_company.smtp_host,
        "port": b_company.smtp_port,
        "username": b_company.smtp_username,
        "password": b_company.smtp_password,
        "from": b_company.smtp_from
    }

    c_smtp = {
        "host": c_company.smtp_host,
        "port": c_company.smtp_port,
        "username": c_company.smtp_username,
        "password": c_company.smtp_password,
        "from": c_company.smtp_from
    }

    d_smtp = {
        "host": d_company.smtp_host,
        "port": d_company.smtp_port,
        "username": d_company.smtp_username,
        "password": d_company.smtp_password,
        "from": d_company.smtp_from
    }

    b_email = b_company.email
    c_email = c_company.email
    d_email = d_company.email

    # 获取对应B公司的邮件模板
    b_email_subject_b3   = render_email_subject("B3", b_company.short_name, project_name, b_company.serial_number)
    b_email_content_b3 = render_invitation_template_content(b_company_name, project_name, "b3_"+b_company.short_name+".txt")
    # 第一封邮件：B ➝ C（立即）
    task1 = send_reply_email.apply_async(
        args=[c_email, b_email_subject_b3, b_email_content_b3, b_smtp],
        countdown=0  # 立即
    )

    # 随机延迟 5–60 分钟
    c_email_subject_b4 = render_email_subject("C3", c_company.short_name, project_name, c_company.serial_number)
    c_email_content_b4 = render_invitation_template_content(c_company_name, project_name, "c3_"+c_company.short_name+".txt")
    delay2 = random.randint(5, 60)
    task2 = send_reply_email.apply_async(
        args=[b_email, c_email_subject_b4, c_email_content_b4, c_smtp],
        countdown=delay2 * 60  # 相对第一封
    )

    # 第三封：B ➝ D（延迟第2封基础上 5–60分钟）
    b_email_subject_b5 = render_email_subject("B5", b_company.short_name, project_name, b_company.serial_number)
    b_email_content_b5 = render_invitation_template_content(b_company_name, project_name, "b5_"+b_company.short_name+".txt")
    delay3 = delay2 + random.randint(5, 60)
    task3 = send_reply_email.apply_async(
        args=[d_email, b_email_subject_b5, b_email_content_b5, b_smtp],
        countdown=delay3 * 60
    )

    # 第四封：D ➝ B（在第3封后延迟 5–60分钟）
    d_email_subject_b6 = render_email_subject("D6", d_company.short_name, project_name, d_company.serial_number)
    d_email_content_b6 = render_invitation_template_content(d_company_name, project_name, "d6_"+d_company.short_name+".txt")
    delay4 = delay3 + random.randint(5, 60)
    task4 = send_reply_email.apply_async(
        args=[b_email, d_email_subject_b6, d_email_content_b6, d_smtp],
        countdown=delay4 * 60
    )

    return {
        "tasks": [
            {"step": "B ➝ C", "task_id": task1.id, "delay_min": 0},
            {"step": "C ➝ B", "task_id": task2.id, "delay_min": delay2},
            {"step": "B ➝ D", "task_id": task3.id, "delay_min": delay3},
            {"step": "D ➝ B", "task_id": task4.id, "delay_min": delay4},
        ]
    }


# CCD 项目类型发送邮件
def schedule_bid_conversation_CCD(b_company_name: str, c_company_name: str, d_company_name: str):
    pass


# BD 项目类型发送邮件
def schedule_bid_conversation_BD(b_company_name: str, d_company_name: str):
    pass
