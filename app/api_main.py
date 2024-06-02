from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import config
from database import init_async_db
from routers import telegram, root, gitlab


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    '''APP Events Listener'''
    await init_async_db()
    yield


app = FastAPI(lifespan=app_lifespan)
app.include_router(root.root_router)
app.include_router(telegram.telegram_router, prefix=config.BOT_PATH)
app.include_router(gitlab.gitlab_router, prefix=config.GITLAB_PATH)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT, reload=False)
