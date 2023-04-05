from sqlalchemy import CHAR, Column, DateTime, Numeric, String, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class GmRegion(Base):
    __tablename__ = 'gmRegion'
    __table_args__ = {'schema': 'dbo'}

    RECORD_STATUS = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    REGIONAL_CODE = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True, server_default=text("('')"))
    REGIONAL_NAME = Column(String(35, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    REGIONAL_MANAGER = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    CHANGE_NO = Column(Numeric(3, 0), nullable=False, server_default=text('((0))'))
    CREATION_USER_ID = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    CHANGE_USER_ID = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False, server_default=text("('')"))
    CREATION_DATETIME = Column(DateTime)
    CHANGE_DATETIME = Column(DateTime)


class GmSArea(Base):
    __tablename__ = 'gmSArea'
    __table_args__ = {'schema': 'dbo'}

    SALES_AREA_CODE = Column(String(5, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    RECORD_STATUS = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    REGIONAL_CODE = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'))
    DESCRIPTION = Column(String(35, 'SQL_Latin1_General_CP1_CI_AS'))
    CHANGE_NO = Column(Numeric(3, 0))
    CREATION_USER_ID = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'))
    CREATION_DATETIME = Column(DateTime)
    CHANGE_USER_ID = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'))
    CHANGE_DATETIME = Column(DateTime)
