from sqlalchemy.orm import Session
from models import dmsmodel
from database.database import engine

def get_data(db:Session):
    res = db.query(dmsmodel.GmRegion).all()
    session = Session(engine)
    coba = db.query(dmsmodel.GmRegion).join(dmsmodel.GmSArea,dmsmodel.GmRegion.REGIONAL_CODE==dmsmodel.GmSArea.REGIONAL_CODE).where(dmsmodel.GmRegion.REGIONAL_CODE=="R01").all()

    return res