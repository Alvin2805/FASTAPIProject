from pydantic import Field,BaseSettings

class Settings(BaseSettings):
    db_user:str = Field(...,env="DB_USER")
    db_password:str = Field(...,env="DB_PASSWORD")
    db_server:str = Field(...,env="DB_SERVER")
    db_name:str = Field(...,env="DB_NAME")

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = "./.env"
        env_file_encoding = "UTF-8"