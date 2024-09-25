from tortoise import Tortoise

from config.settings import DATABASE_URL
from logs.logger import get_logger
logger = get_logger(__name__)

async def init():
    try:
        logger.info("Соединение с базой данных...")
        await Tortoise.init(
            db_url=DATABASE_URL,
            modules={'models': ['app.models']}
        )
        await Tortoise.generate_schemas()
        logger.info("Соединение с базой данных успешно установлено")
    except Exception as e:
        logger.error(f"Ошибка подключения к базе данных: {e}")
        raise

async def close():
    try:
        await Tortoise.close_connections()
        logger.info("Соединение с базой данных завершено")
    except Exception as e:
        logger.error(f"Ошибка при завершении соединения с базой данных: {e}")
        raise
