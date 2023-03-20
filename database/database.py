from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#database_url = "mysql://root:Zhiff%40hmi3310@localhost:3306/sakila" #MYSQL
database_url = "mssql+pymssql://sa:P%40ssw0rd@10.1.32.62/DMSLIVE" #MSSQL SERVER

engine = create_engine(database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()