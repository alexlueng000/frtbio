from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

class EmailRecord(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    to = Column(String(255), nullable=False)         # 收件人邮箱
    subject = Column(String(255))                    # 邮件标题
    body = Column(Text)                              # 邮件正文
    status = Column(String(20), default="pending")   # 邮件状态
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    error_message = Column(Text, nullable=True)      # 错误信息


class CompanyInfo(Base):
    __tablename__ = "company_info"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(255), nullable=False)       # 公司全称
    company_type = Column(String(100))                       # 公司类型
    short_name = Column(String(100))                         # 简称
    contact_person = Column(String(100))                     # 联系人
    last_name = Column(String(100))                          # 姓氏
    last_name_traditional = Column(String(100))              # 姓氏繁体
    phone = Column(String(100))                             # 电话
    email = Column(String(255))                              # 邮箱
    address = Column(String(255))                            # 中文地址
    english_address = Column(String(255))                    # 英文地址
