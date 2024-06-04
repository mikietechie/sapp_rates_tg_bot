from __future__ import annotations
from typing import Optional
from pydantic import BaseModel

# from typing import Any, Optiona


class Client(BaseModel):
    ID: int
    # UpdatedAt: str
    # CreatedAt: str
    # DeletedAt: Any
    api_key: str
    domains: str
    name: str
    reads_available: int
    reads_used: int
    # user_id: int


class CreateClient(BaseModel):
    domains: str
    name: str
    user_id: Optional[int] = 0


class User(BaseModel):
    ID: int
    # CreatedAt: str
    # UpdatedAt: str
    # DeletedAt: Any
    email: str
    password: str
    # role: str
    active: bool


class AuthDataModel(BaseModel):
    user: User
    token: str


class AuthCredentials(BaseModel):
    email: str
    password: str
