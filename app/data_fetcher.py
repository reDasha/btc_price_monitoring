from decimal import Decimal
import aiohttp

from config.settings import BINANCE_API_URL, COINMARKETCAP_API_URL, GATEIO_API_URL, BYBIT_API_URL, KUCOIN_API_URL, \
    COINMARKETCAP_API_KEY
from logs.logger import get_logger

logger = get_logger(__name__)

# Асинхронная функция для получения данных по HTTP-запросу
async def fetch_price(url, headers=None, params=None):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as response:
                return await response.json()
    except aiohttp.ClientError as e:
        logger.error(f"Ошибка при получении данных от {url}: {e}")


# Функция для получения цены BTC/USDT с биржи Binance
async def get_binance_price(pair):
    if pair == 'BTC/USDT':
        pair = 'BTCUSDT'
    else:
        return
    response = await fetch_price(f'{BINANCE_API_URL}?symbol={pair}')
    return Decimal(response['price'])


# Функция для получения цены BTC с сайта CoinMarketCap
async def get_coinmarketcap_price(pair):
    converter = pair.split('/')[-1]
    parameters = {
        'symbol': 'BTC',
        'convert': converter
    }
    headers = {
        'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY
    }
    response = await fetch_price(COINMARKETCAP_API_URL, headers=headers, params=parameters)
    return Decimal(response['data']['BTC']['quote'][converter]['price'])

# Функция для получения цены BTC/USDT с биржи Gate.io
async def get_gateio_price(pair):
    if pair == 'BTC/USDT':
        pair = 'BTC_USDT'
    else:
        return
    response = await fetch_price(f'{GATEIO_API_URL}?currency_pair={pair}')
    return Decimal(response[0]['last'])

# Функция для получения цены BTC/USDT с биржи Bybit
async def get_bybit_price(pair):
    if pair == 'BTC/USDT':
        pair = 'BTCUSDT'
    else:
        return
    response = await fetch_price(f'{BYBIT_API_URL}?symbol={pair}')
    return Decimal(response['result']['price'])

# Функция для получения цены BTC/USDT с биржи Kucoin
async def get_kucoin_price(pair):
    if pair == 'BTC/USDT':
        pair = 'BTC-USDT'
    else:
        return
    response = await fetch_price(f'{KUCOIN_API_URL}?symbol={pair}')
    return Decimal(response['data']['price'])
