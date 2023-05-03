'''
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
'''

from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey
from configs.database import Base

class User(Base):
    __tablename__ = "user"
    __allow_unmapped__ = True
    user_id: Mapped[int] = mapped_column(primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.role_id"))
    name: Mapped[str] | None = None
    email: Mapped[str]
    password: Mapped[str]
    address: Mapped[str] | None = None
    phone_number: Mapped[str] | None = None
    profile_picture: Mapped[str] | None = None
    firebase_token: Mapped[str] | None = None
    is_active: Mapped[bool]

    roles = relationship("Role",back_populates="users")
