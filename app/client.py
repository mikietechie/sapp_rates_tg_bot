import aiohttp

import structs
from cache import rds


class Client(object):
    BASE_URL = "http://localhost:8000/api/v1"

    @classmethod
    async def api_call(cls):
        async with aiohttp.ClientSession() as session:
            res = await session.post(
                f"htpp://localhost:8000/api/v1/auth/login",
                json={"email": "su@mail.com", "password": "password"},
            )
        return None

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
    async def get_client(cls, user: structs.User):
        async with aiohttp.ClientSession() as session:
            res = await session.get(
                f"{cls.BASE_URL}/account/client/using-token", data=user
            )
            res_data: dict = await res.json()
            data = Client(**res_data)
            return data

    @classmethod
    async def create_client(cls, user: structs.User, client: structs.Client):
        async with aiohttp.ClientSession() as session:
            res = await session.post(
                f"{cls.BASE_URL}/account/client/using-token", data=client
            )
            res_data: dict = await res.json()
            data = Client(**res_data)
            return Client
