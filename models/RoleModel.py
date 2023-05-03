'''
from sqlmodel import Field, Relationship,  SQLModel

from models.UserModel import User


class Role(SQLModel, table=True):
    __tablename__ = "role"
    role_id: int = Field(primary_key=True)
    role: str

    users: list[User] = Relationship(back_populates="role")
'''


from sqlalchemy.orm import Mapped,mapped_column, relationship
from configs.database import Base

class Role(Base):
    __tablename__ = "role"
    __allow_unmapped__ = True
    role_id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str]

    users = relationship("User",back_populates="roles")