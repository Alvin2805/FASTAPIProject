from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from configs.connection import Settings

param = Settings()

database_url = f"mssql+pymssql://{param.db_user}:{param.db_password}@{param.db_server}/{param.db_name}"

engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bing=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()