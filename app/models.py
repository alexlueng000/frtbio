from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

class EmailRecord(Base):
    __tablename__ = "emails_records"

    id = Column(Integer, primary_key=True, index=True)
    to = Column(String(255), nullable=False)
    subject = Column(String(255))
    body = Column(Text)
    status = Column(String(20), default="pending")  # pending / success / failed
    task_id = Column(String(100))  # ✅ 新增字段，用于记录 Celery 任务ID
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    error_message = Column(Text, nullable=True)
    project_id = Column(Integer)
    stage = Column(String(12))  
    actual_sending_time = Column(DateTime, nullable=True)
    

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


class ProjectInfo(Base):
    __tablename__ = "project_info"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String(255))
    contract_number = Column(String(100))
    tender_number = Column(String(100)) # 招标编号
    project_type = Column(String(100))  # BCD, CCD, BD
    # project_stage = Column(String(12)) # A, B, C
    p_serial_number = Column(String(100))
    l_serial_number = Column(String(100))
    f_serial_number = Column(String(100))
    purchaser = Column(String(255))
    company_b_name = Column(String(255))
    company_c_name = Column(String(255))
    company_d_name = Column(String(255))
    a1 = Column(Boolean)
    a2 = Column(Boolean)
    b3 = Column(Boolean)
    b4 = Column(Boolean)
    b5 = Column(Boolean)
    b6 = Column(Boolean)
    c7 = Column(Boolean)
    c8 = Column(Boolean)
    c9 = Column(Boolean)
    c10 = Column(Boolean)
    created_at = Column(TIMESTAMP, default=datetime.now(timezone.utc)) # UTC时间




# 邮件标题表
class EmailSubject(Base):

    __tablename__ = "email_subject"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    stage = Column(String(12))
    company_name = Column(String(255))
    short_name = Column(String(100))
    subject = Column(String(255))
    created_at = Column(TIMESTAMP, default=datetime.now(timezone.utc))
    # UTC时间
    subject = Column(String(255))
    created_at = Column(TIMESTAMP, default=datetime.now(timezone.utc))
    # UTC时间
