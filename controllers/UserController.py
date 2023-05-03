from fastapi import APIRouter, Query, status
from sqlalchemy.orm import Session

from configs.database import get_session
from fastapi import Depends
from models.UserModel import User
from payloads.BasePayload import SortEnum, to_model, to_payload
from payloads.UserPayload import CreateUserRequest, UpdateUserRequest
from services import UserService

router = APIRouter(tags=["Users"], prefix="/api")


@router.get("/users")
async def get_users(*, session: Session = Depends(get_session),
                    page: int = 0,
                    page_size: int = 10,
                    filter_by: list[str] = Query([]),
                    filter: list[str] = Query([]),
                    order_by: str = 'user_id',
                    sort: SortEnum = SortEnum.asc):

    results = UserService.get_users(session, page, page_size, filter_by, filter, order_by, sort)

    if not results:
        return to_payload(status_code=status.HTTP_404_NOT_FOUND, message="Data Not Found")

    return to_payload(message="Data Found", data=results)


@router.get("/users/{id}")
async def get_user_by_id(*, session: Session = Depends(get_session),
                         id: int):

    results = UserService.get_user_by_id(session, id)
    print(results)
    if not results:
        return to_payload(status_code=status.HTTP_404_NOT_FOUND, message="Data Not Found")

    return to_payload(message="Data Found", data=results)


@router.post("/users")
async def create_user(*, session: Session = Depends(get_session), request: CreateUserRequest):

    session.begin()

    try:
        UserService.create_user(session, request)
    except Exception as e:
        session.rollback()
        return to_payload(status_code=status.HTTP_409_CONFLICT, message=str(e))

    session.commit()

    return to_payload(status_code=status.HTTP_201_CREATED, message="User Created")


@router.put("/users/{id}")
async def update_user(*, session: Session = Depends(get_session), id: int, request: UpdateUserRequest):

    session.begin()

    try:
        UserService.update_user(session, id, request)
    except Exception as e:
        session.rollback()
        return to_payload(status_code=status.HTTP_409_CONFLICT, message=str(e))

    session.commit()

    return to_payload(message="User Updated")


@router.delete("/users/{id}")
async def delete_user(*, session: Session = Depends(get_session),
                      id: int):

    session.begin()

    try:
        UserService.delete_user(session, id)
    except Exception as e:
        session.rollback()
        return to_payload(status_code=status.HTTP_409_CONFLICT, message=str(e))

    session.commit()

    return to_payload(message="User Deleted")
