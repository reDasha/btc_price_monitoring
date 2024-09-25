import logging

logging.basicConfig(
    filename='logs/log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Функция для получения логгера
def get_logger(name):
    return logging.getLogger(name)