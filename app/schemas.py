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
委托投标登记请求：采购单位，项目名称，流水号，招标编号, B公司名称
'''
class BiddingRegisterRequest(BaseModel):
    purchase_department: str # 采购单位
    b_company_name: str # B公司名称
    project_name: str # 项目名称
    serial_numbers: List[str] # 流水号
    bidding_code: Optional[str] = None # 招标编号



class ProjectInfoOut(BaseModel):
    id: int
    project_name: Optional[str]
    contract_number: Optional[str]
    tender_number: Optional[str]
    project_type: Optional[str]
    p_serial_number: Optional[str]
    l_serial_number: Optional[str]
    f_serial_number: Optional[str]
    purchaser: Optional[str]
    company_b_name: Optional[str]
    company_c_name: Optional[str]
    company_d_name: Optional[str]
    a1: Optional[bool]
    a2: Optional[bool]
    b3: Optional[bool]
    b4: Optional[bool]
    b5: Optional[bool]
    b6: Optional[bool]
    c7: Optional[bool]
    c8: Optional[bool]
    c9: Optional[bool]
    c10: Optional[bool]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)