# app/models.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class EmailRecord(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    to = Column(String, nullable=False)
    subject = Column(String)
    body = Column(Text)
    status = Column(String, default="pending")  # success / failed / pending
    created_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    error_message = Column(Text, nullable=True)


class CompanyInfo(Base):
    __tablename__ = "company_info"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    company_type = Column(String)
    company_alias = Column(String)
    contact_person = Column(String)
    last_name = Column(String)
    last_name_tc = Column(String)
    email = Column(String)
    address = Column(String)
    address_en = Column(String)