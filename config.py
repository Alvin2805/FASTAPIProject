from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

server = "ISIJKTMTMISN109"
database = "testingsales"

#database_url = f"mssql+pymssql://{param.db_user}:{param.db_password}@{param.db_server}:{param.db_port}/{param.db_name}"
database_url = 'mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(database_url)

Local_Session = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = Local_Session()
    try:
        yield db
    finally:
        db.close()