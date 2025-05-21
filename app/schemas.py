# app/schemas.py

from pydantic import BaseModel, EmailStr
from typing import Optional

class CompanyCreate(BaseModel):
    company_name: str
    company_type: Optional[str] = None
    company_alias: Optional[str] = None
    contact_person: Optional[str] = None
    last_name: Optional[str] = None
    last_name_tc: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    address_en: Optional[str] = None

class CompanyInfoOut(CompanyCreate):
    id: int

    class Config:
        orm_mode = True


'''
委托投标登记：采购单位，项目名称，流水号
'''
class BiddingRegisterRequest(BaseModel):
    buyer_name: str
    project_name: str
    serial_number: str