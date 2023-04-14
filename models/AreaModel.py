from typing import Optional
from sqlmodel import Field, SQLModel

class MtrRegion(SQLModel,table=True):
    __tablename__ = "mtr_region"
    is_active:Optional[bool] = Field(nullable=False,default=True)
    area_id:Optional[int] =  Field(primary_key=True)
    area_code:str = Field(nullable=False)
    description:str = Field(nullable=True,default="")
    regional_id:int = Field(default=None,foreign_key="mtr_region.regional_id")