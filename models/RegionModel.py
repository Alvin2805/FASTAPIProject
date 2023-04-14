from typing import Optional
from sqlmodel import SQLModel,Field

class MtrRegion(SQLModel,table=True):
    __tablename__ = "mtr_region"