import asyncio
import schedule
from app.db_init import init, close
from app.monitor import run_monitoring

# Функция для запуска задачи по мониторингу криптобирж
async def job():
    try:
        await run_monitoring()
    except Exception as e:
        print(f"Ошибка при выполнении мониторинга: {e}")

# Функция-планировщик для запуска выполнения задач каждые 10 минут
async def start_scheduler():
    await init()
    try:
        schedule.every(10).minutes.do(lambda: asyncio.create_task(job()))
        while True:
            schedule.run_pending()
            await asyncio.sleep(10)
    finally:
        await close()