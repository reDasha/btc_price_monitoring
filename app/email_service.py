from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import aiosmtplib

from config.settings import MAIL_HOST, MAIL_PORT, EMAIL_SENDER, EMAIL_RECIPIENT
from logs.logger import get_logger

logger = get_logger(__name__)

# Функцяи отправки почты
async def send_email(pair, price, difference):
    currency = pair.split('/')[-1]
    subject = f"Price increase {pair}"
    body = (
        f"Хорошие новости, Лакрица!\n\n"
        f"Цена {pair} выросла на {difference}.\n"
        f"У тебя теперь {(price * 3):,.2f} {currency}. Пойдем тратить!\n"
    )
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECIPIENT
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    try:
        async with aiosmtplib.SMTP(hostname=MAIL_HOST, port=MAIL_PORT) as smtp:
            await smtp.send_message(msg)
        logger.info(f"Email успешно отправлен: {subject}")
    except Exception as e:
        logger.info(f"Ошибка отправки email: {e}")