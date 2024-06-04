import json
import aiohttp

import structs
from cache import rds
from errors import ServiceError


class Service(object):
    BASE_URL = "http://localhost:8000/api/v1"

    @classmethod
    def get_auth_data(cls, username: str):
        user = rds.get(username)
        if user:
            return structs.AuthDataModel(**json.loads(user))

    @classmethod
    def get_headers(cls, auth: structs.AuthDataModel):
        return {"Authorization": f"Bearer {auth.token}"}

    @classmethod
    async def logout(cls, username: str,  auth: structs.AuthDataModel):
        async with aiohttp.ClientSession(headers=cls.get_headers(auth)) as session:
            res = await session.post(
                f"{cls.BASE_URL}/auth/logout",
            )
            await ServiceError.throw(res)
            rds.delete(username)
            return True
        return False

    @classmethod
    async def login(cls, username: str, creds: structs.AuthCredentials):
        async with aiohttp.ClientSession() as session:
            res = await session.post(
                f"{cls.BASE_URL}/auth/login",
                json=creds.model_dump(),
            )
            await ServiceError.throw(res)
            res_data: dict = await res.json()
            obj = structs.AuthDataModel(**res_data)
            print(obj.model_dump_json(indent=4))
            rds.set(username, obj.model_dump_json())
            return obj

    @classmethod
    async def register(cls, username: str, data: structs.AuthCredentials):
        async with aiohttp.ClientSession() as session:
            res = await session.post(f"{cls.BASE_URL}/auth/register", json=data.model_dump())
            await ServiceError.throw(res)
            res_data: dict = await res.json()
            data = structs.AuthDataModel(**res_data)
            rds.set(username, data.model_dump_json())
            return data

    @classmethod
    async def get_client(cls, auth: structs.AuthDataModel):
        async with aiohttp.ClientSession(headers=cls.get_headers(auth)) as session:
            res = await session.get(
                f"{cls.BASE_URL}/account/client/using-token"
            )
            await ServiceError.throw(res)
            res_data: dict = await res.json()
            data = structs.Client(**res_data)
            return data

    @classmethod
    async def create_client(cls, auth: structs.AuthDataModel, data: structs.CreateClient):
        data
        async with aiohttp.ClientSession(headers=cls.get_headers(auth)) as session:
            res = await session.post(
                f"{cls.BASE_URL}/account/client/using-token",
                json=data.model_dump()
            )
            await ServiceError.throw(res)
            res_data: dict = await res.json()
            data = structs.Client(**res_data)
            return structs.Client
