from fastapi import APIRouter,Depends
from cruds import crud
from sqlalchemy.orm import Session
from database.database import get_db

router = APIRouter()
@router.get("/")
def get_all_data(db:Session=Depends(get_db)):
    check = crud.get_data(db)
    return{
        "status" : "Success",
        "results" : len(check),
        "payloads" : check
    }