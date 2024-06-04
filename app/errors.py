from aiohttp import ClientResponse

class ServiceError(Exception):
    @classmethod
    async def throw(cls, res: ClientResponse):
        if not res.ok:
            text = str(await res.read())
            raise ServiceError(f"{res.status} {text}")
    


