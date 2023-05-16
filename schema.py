from pydantic import BaseModel
from datetime import datetime

class MtrAddressSchema(BaseModel):
    is_active:bool
    address_id:int
    address_latitude:float
    address_longitude:float 
    address_street:str 
    address_type:str

class MtrAddressRequest(BaseModel):
    address_latitude:float
    address_longitude:float 
    address_street:str 
    address_type:str

class MtrCitySchema(BaseModel):
    is_active:bool
    city_id:int
    city_name:str
    city_phone:str

class MtrCityRequest(BaseModel):
    city_name:str
    city_phone:str

class MtrProvince(BaseModel):
    is_active:bool
    province_id:int
    province_code:str
    province_name:str

class MtrProvinceRequest(BaseModel):
    province_code:str
    province_name:str

class MtrVillage(BaseModel):
    is_active:bool
    village_id:int
    village_code:str
    village_zip_code:int
    village_name:str

class MtrVillageRequest(BaseModel):
    village_code:str
    village_zip_code:int
    village_name:str

class MtrDistrict(BaseModel):
    is_active:bool
    district_id:int
    district_code:str
    district_name:str

class MtrDistrictRequest(BaseModel):
    district_code:str
    district_name:str

class UserDetailsSchema(BaseModel):
    is_active:bool
    user_employee_id:int
    user_id:int
    employee_name:str
    employee_nickname:str
    id_type:str
    id_no:str
    company_id:int
    job_title_id:int
    job_position_id:int
    divison_id:int
    cost_center_id:int
    profit_center_id:int
    user_bank_account_id:int
    address_id:int
    office_phone_no:str
    home_phone_no:str
    mobile_phone:str
    email_address:str
    start_date:datetime
    termination_date:datetime
    gender:str
    date_of_birth:datetime
    city_of_birth:str
    marital_status:str
    no_of_children:int
    citizenship:str
    last_education:str
    last_employment:str
    factor_x:float 
    skill_level_id:int

class UserDetailsRequest(BaseModel):
    user_id:int
    employee_name:str
    employee_nickname:str
    id_type:str
    id_no:str
    company_id:int
    job_title_id:int
    job_position_id:int
    divison_id:int
    cost_center_id:int
    profit_center_id:int
    user_bank_account_id:int
    address_id:int
    office_phone_no:str
    home_phone_no:str
    mobile_phone:str
    email_address:str
    start_date:datetime
    termination_date:datetime
    gender:str
    date_of_birth:datetime
    city_of_birth:str
    marital_status:str
    no_of_children:int
    citizenship:str
    last_education:str
    last_employment:str
    factor_x:float 
    skill_level_id:int

class UnitInvoiceSchema(BaseModel):
    invoice_system_number:int
    company_id:int
    approval_status_id:int
    bill_to_id_type:str
    bill_to_id_number:str
    bill_to_address_1:str # nama gedung
    bill_to_address_2:str # nama jalan
    village_id:int
    district_id:int
    city_id:int
    province_id:int

class UnitInvoiceRequest(BaseModel):
    company_id:int
    approval_status_id:int
    bill_to_id_type:str
    bill_to_id_number:str
    bill_to_address_1:str # nama gedung
    bill_to_address_2:str # nama jalan
    village_id:int
    district_id:int
    city_id:int
    province_id:int