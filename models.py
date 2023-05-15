from sqlalchemy import String,Column,Float,Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config import Base

class MtrAddress(Base):
    __tablename__ = "mtr_address"
    is_active = Column(Boolean,nullable=False,default=True)
    address_id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    address_latitude = Column(Float,nullable=True,default=0)
    address_longitude = Column(Float,nullable=True,default=0)
    address_street = Column(String(100),nullable=False)
    address_type = Column(String(5),nullable=True,default="")

    users = relationship("UserDetails",back_populates="addresses")

class MtrCity(Base):
    __tablename__ = "mtr_city"
    is_active = Column(Boolean,nullable=False)
    city_id = Column(Integer, primary_key=True,autoincrement=True)
    city_name = Column(String,nullable=False)
    city_phone = Column(String,nullable=False)
    
    unitinvoices4 = relationship("UnitInvoice",back_populates="users_city")

class MtrProvince(Base):
    __tablename__ = "mtr_province"
    is_active = Column(Boolean,nullable=False)
    province_id = Column(Integer,primary_key=True,autoincrement=True)
    province_code = Column(String, nullable=False)
    province_name = Column(String, nullable=False)

    unitinvoices1 = relationship("UnitInvoice",back_populates="users_province")

class MtrVillage(Base):
    __tablename__ = "mtr_village"
    is_active = Column(Boolean,nullable=False)
    village_id = Column(Integer,primary_key=True,autoincrement=True)
    village_code = Column(String,nullable=False)
    village_zip_code = Column(Integer, nullable=False)
    village_name = Column(String, nullable=False)

    unitinvoices2 = relationship("UnitInvoice",back_populates="users_village")

class MtrDistrict(Base):
    __tablename__ = "mtr_district"
    is_active = Column(Boolean,nullable=False)
    district_id = Column(Integer, primary_key=True, autoincrement=True)
    district_code = Column(String, nullable=False)
    district_name = Column(String, nullable=False)

    unitinvoices3 = relationship("UnitInvoice",back_populates="users_district")

class UserDetails(Base):
    __tablename__ = "mtr_user_details"
    is_active = Column(Boolean,nullable=False)
    user_employee_id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer, nullable=False)
    employee_name = Column(String,nullable=False)
    employee_nickname = Column(String,nullable=False)
    id_type = Column(String,nullable=False)
    id_no = Column(String,nullable=False)
    company_id = Column(Integer,nullable=False)
    job_title_id = Column(Integer,nullable=False)
    job_position_id = Column(Integer, nullable=False)
    divison_id = Column(Integer,nullable=False)
    cost_center_id = Column(Integer,nullable=False)
    profit_center_id = Column(Integer,nullable=False)
    user_bank_account_id = Column(Integer,nullable=False)
    address_id = Column(Integer,ForeignKey("mtr_address.address_id"))
    office_phone_no = Column(String,nullable=False)
    home_phone_no = Column(String, nullable=False)
    mobile_phone = Column(String, nullable=False)
    email_address = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=True)
    termination_date = Column(DateTime, nullable=True)
    gender = Column(String, nullable=True)
    date_of_birth = Column(DateTime, nullable=True)
    city_of_birth = Column(String, nullable=True)
    marital_status = Column(String, nullable=True)
    no_of_children = Column(Integer,nullable=True)
    citizenship = Column(String,nullable=True)
    last_education = Column(String, nullable=True)
    last_employment = Column(String, nullable=True)
    factor_x = Column(Float,nullable=False)
    skill_level_id = Column(Integer, nullable=False)

    addresses = relationship("MtrAddress", back_populates="users")

class UnitInvoice(Base):
    __tablename__ = "unit_invoice"
    invoice_system_number = Column(Integer, primary_key=True,autoincrement=True)
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
    village_id = Column(Integer, ForeignKey("mtr_village.village_id")) # mtr_village
    district_id = Column(Integer, ForeignKey("mtr_district.district_id")) # mtr_district
    city_id = Column(Integer, ForeignKey("mtr_city.city_id")) # mtr_city
    province_id = Column(Integer, ForeignKey("mtr_province.province_id")) # mtr_province
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

    users_province = relationship("MtrProvince",back_populates="unitinvoices1")
    users_village = relationship("MtrVillage",back_populates="unitinvoices2")
    users_district = relationship("MtrDistrict",back_populates="unitinvoices3")
    users_city = relationship("MtrCity",back_populates="unitinvoices4")