from __future__ import annotations
from typing import Any
from pydantic import BaseModel
import aiohttp

# from typing import Any, Optiona


class Client(BaseModel):
    api_key: str
    createdAt: str
    deletedAt: Any
    domains: str
    id: int
    name: str
    reads_available: int
    reads_used: int
    updatedAt: str
    user_id: int


class User(BaseModel):
    ID: int
    CreatedAt: str
    UpdatedAt: str
    DeletedAt: Any
    email: str
    password: str
    role: str
    active: bool


class AuthDataModel(BaseModel):
    user: User
    token: str


class AuthCredentials(BaseModel):
    email: str
    password: str
