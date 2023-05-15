from pydantic import BaseModel
from datetime import datetime

class MtrAddressSchema(BaseModel):
    is_active:bool
    address_id:int
    address_latitude:float
    address_longitude:float 
    address_street:str 
    address_type:str

class UserDetails(BaseModel):
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

class UnitInvoice(Base):
    __tablename__ = "trx_account_receivable"
    invoice_system_number = Column(Integer, primary_key=True)
    company_id = Column(Integer,nullable=False)
    approval_status_id = Column(Integer, nullable=False)
    invoice_document_number = Column(Integer, nullable=False)
    account_receivable_invoice_type_id = Column(Integer, nullable=False)
    invoice_date = Column(DateTime, nullable=False)
    invoice_due_date = Column(DateTime, nullable=False)
    remark = Column(String,nullable=False)
    brand_id = Column(Integer, nullable=False)
    profit_center_id = Column(Integer, nullable=False)
    transaction_type_id = Column(Integer, nullable=False)
    event_id = Column(Integer, nullable=False)
    event_id = Column(Integer, nullable=False)
    workorder_transaction_type_id = Column(Integer, nullable=False)
    customer_type_id = Column(Integer, nullable=False)
    customer_id = Column(Integer, nullable=False)
    fund_type_id = Column(Integer, nullable=False)
    sales_representative_id = Column(Integer, nullable=False)
    currency_id = Column(Integer, nullable=False)
    currency_exchange_rate_type = Column(String,nullable=False)
    currency_exchange_rate_date = Column(DateTime)
    currency_exchange_rate = Column(Float)
    tax_exchange_rate_type  = Column(String)
    tax_exchange_rate_date = Column(DateTime)
    tax_exchange_rate = Column(Float)
    leasing_supplier_code = Column(String)
    purchase_order_system_number = Column(Integer)
    purchase_order_document_number = Column(String)
    reference_type = Column(String)
    reference_system_number = Column(Integer)
    reference_document_number = Column(String)
    reference_tnkb = Column(String)
    reference_insurance_policy_number = Column(String)
    reference_service_advisor = Column(String)
    reference_contract_service_code = Column(String)
    reference_document_date = Column(DateTime)
    reference_invoice_due_date = Column(DateTime)
    reference_total = Column(Float)
    reference_total_base_amount = Column(Float)
    reference_second_type = Column(String)
    reference_second_system_number = Column(Integer)
    reference_second_document_number = Column(String)
    billable_to_id = Column(Integer, nullable=False)
    bill_to_customer_type = Column(String)
    bill_to_customer_code = Column(String)
    bill_to_title_prefix = Column(String)
    bill_to_name = Column(String)
    bill_to_title_suffix = Column(String)
    bill_to_id_type = Column(String)
    bill_to_id_number = Column(String)
    bill_to_address_1 = Column(String) # nama gedung
    bill_to_address_2 = Column(String) # nama jalan
    village_id = Column(Integer)
    district_id = Column(Integer)
    city_id = Column(Integer)
    province_id = Column(Integer)
    city_id = Column(Integer)
    village_id = Column(Integer)
    bill_to_phone_number = Column(String)
    bill_to_fax = Column(String)
    bill_to_tax_registration_number = Column(String)
    bill_to_registration_date = Column(DateTime)
    top_id = Column(Integer)
    pay_type = Column(String)
    reference_id = Column(Integer)
    vat_percent = Column(Float)
    vat_tax_type = Column(String)
    vat_service_code = Column(String)
    pkp_type = Column(String)
    pkp_number = Column(String)
    pkp_date = Column(DateTime)
    tax_name = Column(String)
    tax_address_1 = Column(String)
    tax_address_2 = Column(String)
    village_id = Column(Integer)
    district_id = Column(Integer)
    city_id = Column(Integer)
    province_id = Column(Integer)
    city_id = Column(Integer)
    village_id = Column(Integer)
    tax_invoice_system_number = Column(Integer)
    tax_invoice_document_number = Column(String)
    tax_invoice_date = Column(DateTime)
    tax_invoice_id = Column(Integer)
    reference_tax_invoice_system_number = Column(Integer)
    reference_tax_invoice_document_number = Column(String)
    reference_tax_invoice_date = Column(DateTime)
    invoice_payable_system_no = Column(Integer)