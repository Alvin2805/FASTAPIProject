from fastapi import APIRouter, Depends
from config import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import MtrAddress,MtrCity,MtrDistrict,MtrProvince,MtrVillage,UserDetails, UnitInvoice
from schema import MtrAddressRequest,MtrCityRequest,MtrVillageRequest,MtrProvinceRequest,MtrDistrictRequest,UserDetailsRequest,UnitInvoiceRequest

router = APIRouter(tags=["Simulasi"],prefix="/api/coba")

@router.post("/address")
async def post_address(req_data:MtrAddressRequest,db:Session=Depends(get_db)):
    inp_data = MtrAddress()
    inp_data.address_latitude = req_data.address_latitude
    inp_data.address_longitude = req_data.address_longitude
    inp_data.address_street = req_data.address_street
    inp_data.address_type = req_data.address_type
    db.add(inp_data)
    db.commit()
    db.refresh(inp_data)
    return inp_data

@router.post("/city")
async def post_city(req_data:MtrCityRequest,db:Session=Depends(get_db)):
    inp_data = MtrCity()
    inp_data.city_name = req_data.city_name
    inp_data.city_phone = req_data.city_phone
    db.add(inp_data)
    db.commit()
    db.refresh(inp_data)
    return inp_data

@router.post("/province")
async def post_province(req_data:MtrProvinceRequest,db:Session=Depends(get_db)):
    inp_data = MtrProvince()
    inp_data.province_code = req_data.province_code
    inp_data.province_name = req_data.province_name
    db.add(inp_data)
    db.commit()
    db.refresh(inp_data)
    return inp_data

@router.post("/village")
async def post_village(req_data:MtrVillageRequest,db:Session=Depends(get_db)):
    inp_data = MtrVillage()
    inp_data.village_code = req_data.village_code
    inp_data.village_name = req_data.village_name
    inp_data.village_zip_code = req_data.village_zip_code
    db.add(inp_data)
    db.commit()
    db.refresh(inp_data)
    return inp_data

@router.post("/district")
async def post_district(req_data:MtrDistrictRequest,db:Session=Depends(get_db)):
    inp_data = MtrDistrict()
    inp_data.district_code = req_data.district_code
    inp_data.district_name = req_data.district_name
    db.add(inp_data)
    db.commit()
    db.refresh(inp_data)
    return inp_data

@router.post("/users")
async def post_user(req_data:UserDetailsRequest,db:Session=Depends(get_db)):
    inp_data = UserDetails()
    inp_data.user_id = req_data.user_id
    inp_data.employee_name = req_data.employee_name
    inp_data.employee_nickname = req_data.employee_nickname
    inp_data.id_type = req_data.id_type
    inp_data.id_no = req_data.id_no
    inp_data.company_id = req_data.company_id
    inp_data.job_title_id = req_data.job_title_id
    inp_data.job_position_id = req_data.job_position_id
    inp_data.divison_id = req_data.divison_id
    inp_data.cost_center_id = req_data.cost_center_id
    inp_data.profit_center_id = req_data.profit_center_id
    inp_data.user_bank_account_id = req_data.user_bank_account_id
    inp_data.address_id = req_data.address_id
    inp_data.office_phone_no = req_data.office_phone_no
    inp_data.home_phone_no = req_data.home_phone_no
    inp_data.mobile_phone = req_data.mobile_phone
    inp_data.email_address = req_data.email_address
    inp_data.start_date = req_data.start_date
    inp_data.termination_date = req_data.termination_date
    inp_data.gender = req_data.gender
    inp_data.date_of_birth = req_data.date_of_birth
    inp_data.city_of_birth = req_data.city_of_birth
    inp_data.marital_status = req_data.marital_status
    inp_data.no_of_children = req_data.no_of_children
    inp_data.citizenship = req_data.citizenship
    inp_data.last_education = req_data.last_education
    inp_data.last_employment = req_data.last_employment
    inp_data.factor_x = req_data.factor_x
    inp_data.skill_level_id = req_data.skill_level_id
    db.add(inp_data)
    db.commit()
    db.refresh(inp_data)
    return inp_data

@router.post("/invoice")
async def post_invoice(req_data:UnitInvoiceRequest,db:Session=Depends(get_db)):
    inp_data = UnitInvoice()
    inp_data.company_id = req_data.company_id
    inp_data.approval_status_id = req_data.approval_status_id
    inp_data.bill_to_id_type = req_data.bill_to_id_type
    inp_data.bill_to_id_number = req_data.bill_to_id_number

    #get the adddress based on user id
    usr = get_users_by_id(inp_data.company_id,db)
    address = get_address_by_id(usr.address_id,db)
    
    inp_data.bill_to_address_1 = req_data.bill_to_address_1
    inp_data.bill_to_address_2 = req_data.bill_to_address_2
    inp_data.village_id = req_data.village_id
    inp_data.district_id =  req_data.district_id
    inp_data.city_id = req_data.city_id
    inp_data.province_id = req_data.province_id

    if req_data.bill_to_address_1 != address.address_street or req_data.bill_to_address_2 != address.address_type:
        new_data = MtrAddress()
        new_data.address_street = inp_data.bill_to_address_1
        new_data.address_type = inp_data.bill_to_address_2
        updated_id = post_address(new_data,db)
        update_user_address(inp_data.company_id,updated_id,db)

    db.add(inp_data)
    db.commit()
    db.refresh(inp_data)

    return inp_data

@router.get("/address")
async def get_address(db:Session=Depends(get_db)):
    get_data = select(MtrAddress)
    results = db.scalars(get_data).all()  
    return results

@router.get("/city")
async def get_city(db:Session=Depends(get_db)):
    get_data = select(MtrCity)
    results = db.scalars(get_data).all()
    return results

@router.get("/province")
async def get_province(db:Session=Depends(get_db)):
    get_data = select(MtrProvince)
    results = db.scalars(get_data).all()
    return results

@router.get("/village")
async def get_village(db:Session=Depends(get_db)):
    get_data = select(MtrVillage)
    results = db.scalars(get_data).all()
    return results

@router.get("/district")
async def get_district(db:Session=Depends(get_db)):
    get_data = select(MtrDistrict)
    results = db.scalars(get_data).all()
    return results

@router.get("/user")
async def get_user(db:Session=Depends(get_db)):
    get_data = select(UserDetails)
    results = db.scalars(get_data).all()
    return results

@router.get("/invoice")
async def get_invoice(db:Session=Depends(get_db)):
    get_invoice = select(UnitInvoice)
    results = db.scalars(get_invoice).all()
    return results

@router.put("/user")
async def cobaupdate(id:int,new_data:int,db:Session=Depends(get_db)):
    get_user = get_users_by_id(id,db)
    get_user.address_id = new_data
    db.commit()
    db.refresh(get_user)
    return get_user

def get_users_by_id(id:int,db:Session):
    user_by_id = select(UserDetails).where(UserDetails.user_employee_id==id).order_by(UserDetails.user_employee_id.desc())
    user = db.scalars(user_by_id).first()
    return user

def get_address_by_id(id:int,db:Session):
    address_by_id = select(MtrAddress).where(MtrAddress.address_id==id).order_by(MtrAddress.address_id.desc())
    address = db.scalars(address_by_id).first()
    return address

def post_address(req_data:MtrAddressRequest,db:Session):
    inp_data = MtrAddress()
    inp_data.address_latitude = req_data.address_latitude
    inp_data.address_longitude = req_data.address_longitude
    inp_data.address_street = req_data.address_street
    inp_data.address_type = req_data.address_type
    db.add(inp_data)
    db.commit()
    db.refresh(inp_data)
    return inp_data.address_id

def update_user_address(id:int,new_data:int,db:Session):
    get_user = get_users_by_id(id,db)
    get_user.address_id = new_data
    db.commit()
    db.refresh(get_user)