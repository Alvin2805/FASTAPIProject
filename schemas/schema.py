from typing import List
from pydantic import BaseModel

class RegionSchema(BaseModel):
    RECORD_STATUS:str
    REGIONAL_CODE:str
    REGIONAL_NAME:str
    REGIONAL_MANAGER:str
    CHANGE_NO:int
    CREATION_USER_ID:str
    CHANGE_USER_ID:str
    CREATION_DATETIME:str
    CHANGE_DATETIME:str

    class Config:
        orm_mode = True

class RegionResponse(BaseModel):
    status:str
    results:int
    payloads:List[RegionSchema]


class AreaSchema(BaseModel):
    SALES_AREA_CODE:str
    RECORD_STATUS:str
    REGIONAL_CODE:str
    DESCRIPTION:str
    CHANGE_NO:int
    CREATION_USER_ID:str
    CREATION_DATETIME:str
    CHANGE_USER_ID:str
    CHANGE_DATETIME:str

    class Config:
        orm_mode = True

class AreaResponse(BaseModel):
    status:str
    results:int
    payloads:List[AreaSchema]
