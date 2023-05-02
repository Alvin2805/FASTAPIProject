from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str
    address: str
    phone_number: str


class UpdateUserRequest(BaseModel):
    name: str
    email: str
    password: str
    address: str
    phone_number: str
    profile_picture: str | None


class UserResponse(BaseModel):
    name: str
    email: str
    address: str
    phone_number: str
    profile_picture: str | None
    role_id: int
    role: str
    is_active: bool
