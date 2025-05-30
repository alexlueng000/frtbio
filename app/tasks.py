
# app/tasks.py
# 处理B公司回复邮件的任务

from celery import Celery
from sqlalchemy.orm import Session
from app import email_utils, models, database

celery = Celery(
    "syjz_emails",
    broker="redis://localhost:6379/0",      # Redis 作为 broker
    backend="redis://localhost:6379/0"      # 可用于任务结果存储（可选）
)

@celery.task
def send_reply_email(to_email: str, subject: str, content: str, smtp_config: dict):
    email_utils.send_email(to_email, subject, content, smtp_config)
    
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

