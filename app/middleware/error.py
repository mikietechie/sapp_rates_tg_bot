from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram import types
from aiohttp.client import ClientResponseError

from errors import ServiceError


class ErrorMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        pass

    async def __call__(
        self,
        handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]],
        event: types.Message,
        data: Dict[str, Any]
    ) -> Any:
        try:
            return await handler(event, data)
        except Exception as e:
            if isinstance(e, (ServiceError, ClientResponseError)):
                await event.answer(text=f"Error\n{e}")
            else:
                await event.answer(
                    text="Opps ,An Error Occured please contact the developers, or retry."
                )
            print(e.with_traceback(None))
