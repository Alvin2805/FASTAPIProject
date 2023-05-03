
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from configs.config import Settings
from sqlalchemy.orm import declarative_base

Base = declarative_base()

check = Settings()

# MSSQL SERVER
database_url = f"mssql+pymssql://{check.db_user}:{check.db_password}@{check.db_server}/{check.db_name}"


engine = create_engine(database_url, echo=False)


def get_session():
    with Session(engine) as session:
        yield session
