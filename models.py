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
    is_active = Column(Boolean,nullable=False,default=True)
    city_id = Column(Integer, primary_key=True,autoincrement=True)
    city_name = Column(String,nullable=False)
    city_phone = Column(String,nullable=False)

    city_invoices = relationship("UnitInvoice",back_populates="cities")


class MtrProvince(Base):
    __tablename__ = "mtr_province"
    is_active = Column(Boolean,nullable=False, default=True)
    province_id = Column(Integer,primary_key=True,autoincrement=True)
    province_code = Column(String, nullable=False)
    province_name = Column(String, nullable=False)

    province_invoices = relationship("UnitInvoice", back_populates="provinces")


class MtrVillage(Base):
    __tablename__ = "mtr_village"
    is_active = Column(Boolean,nullable=False,default=True)
    village_id = Column(Integer,primary_key=True,autoincrement=True)
    village_code = Column(String,nullable=False)
    village_zip_code = Column(Integer, nullable=False)
    village_name = Column(String, nullable=False)

    village_invoices = relationship("UnitInvoice",back_populates="villages")


class MtrDistrict(Base):
    __tablename__ = "mtr_district"
    is_active = Column(Boolean,nullable=False,default=True)
    district_id = Column(Integer, primary_key=True, autoincrement=True)
    district_code = Column(String, nullable=False)
    district_name = Column(String, nullable=False)

    district_invoices = relationship("UnitInvoice",back_populates="districts")


class UserDetails(Base):
    __tablename__ = "mtr_user_details"
    is_active = Column(Boolean,nullable=False,default=True)
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
    bill_to_id_type = Column(String)
    bill_to_id_number = Column(String)
    bill_to_address_1 = Column(String) # nama gedung
    bill_to_address_2 = Column(String) # nama jalan
    village_id = Column(Integer, ForeignKey("mtr_village.village_id")) # mtr_village
    district_id = Column(Integer, ForeignKey("mtr_district.district_id")) # mtr_district
    city_id = Column(Integer, ForeignKey("mtr_city.city_id")) # mtr_city
    province_id = Column(Integer, ForeignKey("mtr_province.province_id")) # mtr_province

    villages = relationship("MtrVillage",back_populates="village_invoices")
    cities = relationship("MtrCity",back_populates="city_invoices")
    districts = relationship("MtrDistrict",back_populates="district_invoices")
    provinces = relationship("MtrProvince",back_populates="province_invoices")