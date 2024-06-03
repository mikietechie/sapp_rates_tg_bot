import json
import aiohttp

import structs
from cache import rds


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
            await session.post(
                f"{cls.BASE_URL}/auth/logout",
            )
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
            res_data: dict = await res.json()
            obj = structs.AuthDataModel(**res_data)
            print(obj.model_dump_json(indent=4))
            rds.set(username, obj.model_dump_json())
            return obj

    @classmethod
    async def register(cls, username: str, user: structs.User):
        async with aiohttp.ClientSession() as session:
            res = await session.post(f"{cls.BASE_URL}/auth/register", data=user)
            res_data: dict = await res.json()
            data = structs.AuthDataModel(**res_data)
            rds.set(username, data.model_dump_json)
            return data

    @classmethod
    async def get_client(cls, auth: structs.AuthDataModel):
        async with aiohttp.ClientSession(headers=cls.get_headers(auth)) as session:
            res = await session.get(
                f"{cls.BASE_URL}/account/client/using-token"
            )
            res_data: dict = await res.json()
            data = structs.Client(**res_data)
            return data

    @classmethod
    async def create_client(cls, auth: structs.AuthDataModel, client: structs.Client):
        async with aiohttp.ClientSession(headers=cls.get_headers(auth)) as session:
            res = await session.post(
                f"{cls.BASE_URL}/account/client/using-token"
            )
            res_data: dict = await res.json()
            data = structs.Client(**res_data)
            return structs.Client
