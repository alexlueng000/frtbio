
# app/tasks.py
# 处理B公司回复邮件的任务

import time
import smtplib
from email.mime.text import MIMEText

from celery import Celery
from sqlalchemy.orm import Session
from app import email_utils, models, database


celery = Celery(
    "syjz_emails",
    broker="redis://localhost:6379/0",      # Redis 作为 broker
    backend="redis://localhost:6379/0"      # 可用于任务结果存储（可选）
)


def send_sync_email(to_email, subject, content, smtp_config):
    msg = MIMEText(content, "html", "utf-8")
    msg["From"] = smtp_config["from"]
    msg["To"] = to_email
    msg["Subject"] = subject

    try:
        server = smtplib.SMTP_SSL(smtp_config["host"], smtp_config["port"])
        server.login(smtp_config["username"], smtp_config["password"])
        server.sendmail(smtp_config["from"], [to_email], msg.as_string())
        server.quit()
        return True, ""
    except Exception as e:
        return False, str(e)


@celery.task
def test_task(msg: str):
    print(f"[Celery 执行任务] {time.strftime('%H:%M:%S')} - 收到消息：{msg}")
    return {"msg": msg}


@celery.task
def send_reply_email(to_email: str, subject: str, content: str, smtp_config: dict):

    db = database.SessionLocal()
    success, error = email_utils.send_email(to_email, subject, content, smtp_config)
    
    # 需要更新这个邮件发送记录
    record = models.EmailRecord(
        to=to_email,
        subject=subject,
        body=content,
        status="success" if success else "failed",
        error_message=error if not success else None
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return {"success": success, "error": error}


