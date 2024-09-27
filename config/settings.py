import os

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')

DATABASE_URL = f"postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

MAIL_HOST = os.getenv('MAIL_HOST')
MAIL_PORT = os.getenv('MAIL_PORT')
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_RECIPIENT = os.getenv('EMAIL_RECIPIENT')
COINMARKETCAP_API_KEY = os.getenv('COINMARKETCAP_API_KEY')

BINANCE_API_URL = "https://api.binance.com/api/v3/ticker/price"
COINMARKETCAP_API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
GATEIO_API_URL = "https://api.gateio.ws/api/v4/spot/tickers"
BYBIT_API_URL = "https://api.bybit.com/spot/v3/public/quote/ticker/price"
KUCOIN_API_URL = "https://api.kucoin.com/api/v1/market/orderbook/level1"

