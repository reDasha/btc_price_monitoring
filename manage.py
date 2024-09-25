import asyncio
from app.db_init import init
from app.scheduler import start_scheduler

async def main():
    await init()
    await start_scheduler()

if __name__ == "__main__":
    asyncio.run(main())
