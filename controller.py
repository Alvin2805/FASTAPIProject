from fastapi import APIRouter, Depends
from config import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import MtrAddress,MtrCity,MtrDistrict,MtrProvince,MtrVillage,UserDetails

router = APIRouter(tags=["Simulasi"],prefix="/api/coba")

@router.get("/address")
async def get_address(db:Session=Depends(get_db)):
    get_data = select(MtrAddress)
    results = db.scalars(get_data).all()  
    return results
