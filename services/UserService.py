#from sqlmodel import Session, column, select
from sqlalchemy.orm import Session
from sqlalchemy import select, column
from fastapi.encoders import jsonable_encoder
from models.UserModel import User
from payloads.UserPayload import CreateUserRequest
from utils.Parse import strtobool


def get_users(session: Session, page: int, page_size: int, filter_by: list[str], filter: list[str],  order_by: str, sort: str):

    user = select(User)

    if (sort == 'asc'):
        user = user.order_by(column(order_by).asc())
    else:
        user = user.order_by(column(order_by).desc())

    user = user.offset(page*page_size).limit(page_size)

    if (len(filter) > 0):
        for idx, x in enumerate(filter):

            if (filter_by[idx] == "is_active"):
                user = user.filter(column(filter_by[idx]) == strtobool(filter[idx]))
                continue

            user = user.filter(column(filter_by[idx]).contains(filter[idx]))

    return session.exec(user).all()


def get_user_by_id(session: Session, id: int):

    user = select(User.user_id, User.role, User.email).where(User.user_id == id)

    return jsonable_encoder(session.exec(user).first())


def create_user(session: Session, request: CreateUserRequest):

    user = User(role_id=1,
                name=request.name,
                email=request.email,
                password=request.password,
                address=request.address,
                phone_number=request.phone_number,
                is_active=False)

    return session.add(user)


def update_user(session: Session, id: int, request: CreateUserRequest):

    user = select(User).where(User.user_id == id)
    current_user = session.exec(user).first()
    current_user.name = request.name
    current_user.email = request.email
    current_user.password = request.password
    current_user.address = request.address
    current_user.phone_number = request.phone_number
    current_user.profile_picture = request.profile_picture

    return session.add(current_user)


def delete_user(session: Session, id: int):

    user = select(User).where(User.user_id == id)
    current_user = session.exec(user).first()

    return session.delete(current_user)
