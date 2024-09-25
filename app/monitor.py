from decimal import Decimal

from app.data_fetcher import get_binance_price, get_gateio_price, get_bybit_price, get_kucoin_price, \
    get_coinmarketcap_price
from app.database_manager import save_to_db
from app.email_service import send_email

pairs = ['BTC/RUB', 'BTC/USDT', 'BTC/ETH', 'BTC/SOL', 'BTC/DOGE']
fetch_funcs = [
    get_binance_price,
    get_gateio_price,
    get_bybit_price,
    get_kucoin_price,
    get_coinmarketcap_price
]

# Функция для мониторинга цен разных валютных пар на пяти биржах
async def run_monitoring():
    for fetch_func in fetch_funcs:
        for pair in pairs:
            current_price = await fetch_func(pair)

            if current_price:
                last_price, difference = await save_to_db(current_price, pair)
                if current_price > last_price * Decimal(1.0003):
                    await send_email(pair, current_price, round(difference, 4))
