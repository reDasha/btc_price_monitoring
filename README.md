# BTC Price Monitoring Project

## Описание

Этот проект предназначен для мониторинга цен на BTC (Bitcoin) на различных криптовалютных биржах и отправки уведомления о значительных изменениях в цене на email. Проект использует асинхронное программирование для работы с API пяти криптовалютных бирж, отслеживая изменения шести валютных пар:
- BTC/USDT
- BTC/ETH
- BTC/XMR
- BTC/SOL
- BTC/RUB
- BTC/DOGE

## Структура проекта

- `app/`: Основной код приложения.
  - `data_fetcher.py`: Функции для получения цен с разных бирж.
  - `database_manager.py`: Функции для работы с базой данных.
  - `email_service.py`: Функции для отправки email-уведомлений.
  - `monitor.py`: Функции для мониторинга цен и сохранения данных.
  - `scheduler.py`: Планировщик задач для регулярного мониторинга.
  - `data_to_csv.py`: Функции для записи данных в csv-файл.
  - `models.py`: Модели базы данных.
  - `db_init.py`: Инициализация базы данных.

## Установка

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/reDasha/btc_price_monitoring.git
cd btc_price_monitoring
```

### 2. Создайте файл .env

Создайте файл `.env` в корневой директории проекта и добавьте в него указанные переменные окружения. Этот файл содержит индивидуальную и конфиденциальную информацию.

Пример содержания файла `.env`:

```env
DB_HOST=host.docker.internal
DB_PORT=5432
DB_NAME=btc_data
DB_USER=postgres
DB_PASS=postgres
MAIL_HOST=mailcatcher
MAIL_PORT=1025
EMAIL_SENDER=user@yandex.ru
EMAIL_RECIPIENT=user@yandex.ru
COINMARKETCAP_API_KEY=your-api-key
```

### 3. Запустите проект
```bash
docker-compose up --build
```
Docker compose автоматически соберет docker-образ приложения, запустит его, а также запустит базу данных PostgreSQL и Mailcatcher.

После выполнения этой команды проект будет доступен по следующим адресам:

- MailСatcher: http://0.0.0.0:1080
- PostgreSQL: 0.0.0.0:5432