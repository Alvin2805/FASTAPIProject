from sqlmodel import Field, Relationship,  SQLModel

from models.RoleModel import Role


class User(SQLModel, table=True):
    __tablename__ = "user"
    user_id: int = Field(primary_key=True)
    role_id: int = Field(foreign_key="role.role_id")
    name: str | None = None
    email: str
    password: str
    address: str | None = None
    phone_number: str | None = None
    profile_picture: str | None = None
    firebase_token: str | None = None
    is_active: bool

    role: Role = Relationship(back_populates="users")
