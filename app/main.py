import asyncio

from telegram.main import bootstrap_bot


async def main():
    await bootstrap_bot()


if __name__ == "__main__":
    asyncio.run(main())
