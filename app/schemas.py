# app/schemas.py

from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List

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

    model_config = ConfigDict(from_attributes=True)


'''
委托投标登记：采购单位，项目名称，流水号
'''
class BiddingRegisterRequest(BaseModel):
    buyer_name: str # B公司名称
    project_name: str # 项目名称
    serial_number: List[str] # 流水号