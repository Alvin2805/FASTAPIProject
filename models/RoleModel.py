from sqlmodel import Field, Relationship,  SQLModel

from models.UserModel import User


class Role(SQLModel, table=True):
    __tablename__ = "role"
    role_id: int = Field(primary_key=True)
    role: str

    users: list[User] = Relationship(back_populates="role")
