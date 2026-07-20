from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ProfileBase(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    phone: str = Field(min_length=3, max_length=50)
    address: str = Field(min_length=3, max_length=200)


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=120)
    phone: str | None = Field(default=None, min_length=3, max_length=50)
    address: str | None = Field(default=None, min_length=3, max_length=200)


class ProfileOut(ProfileBase):
    id: str
    user_id: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)
    name: str = Field(min_length=1, max_length=120)
    phone: str = Field(min_length=3, max_length=50)
    address: str = Field(min_length=3, max_length=200)


class UserUpdate(BaseModel):
    email: EmailStr | None = None


class UserOut(BaseModel):
    id: str
    email: EmailStr
    is_active: bool
    role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class AuthMeResponse(BaseModel):
    email: EmailStr
    profile: ProfileOut
