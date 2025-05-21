# app/email_utils.py
from aiosmtplib import SMTP
from email.message import EmailMessage

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
