from datetime import datetime

from tortoise.exceptions import DoesNotExist

from app.data_to_csv import save_to_csv
from app.models import BTCPrice


# Функция для сохранения в базу данных
async def save_to_db(price, pair):
    last_pair_entry = await BTCPrice.filter(title=pair).order_by('-date').first()
    last_pair_price = last_pair_entry.price if last_pair_entry else price

    max_price_entry = await BTCPrice.filter(title=pair).order_by('-price').first()
    max_pair_price = max(max_price_entry.price, price) if max_price_entry else price

    min_price_entry = await BTCPrice.filter(title=pair).order_by('price').first()
    min_pair_price = min(min_price_entry.min_price, price) if min_price_entry else price

    difference = round((price - last_pair_price), 4)
    amount = price * 3
    date_iso = datetime.now().isoformat()

    await BTCPrice.create(
        title=pair,
        price=price,
        max_price=max_pair_price,
        min_price=min_pair_price,
        difference=difference,
        total_amount=amount,
        date=date_iso
    )

    await save_to_csv(pair, round(price, 5), round(max_pair_price, 5), round(min_pair_price, 5), date_iso, difference, round(amount, 5))

    return last_pair_price, difference


# Функция для поиска записей из базы по названию пары
async def search_by_title(title):
    records = await BTCPrice.filter(title=title).all()
    return records


# Функция для поиска записей из базы по id
async def search_by_id(record_id):
    record = await BTCPrice.filter(id=record_id).all()
    return record


# Функция для удаления записей из базы по названию пары
async def delete_pairs_from_db(title):
    deleted_cnt = await BTCPrice.filter(title=title).delete()
    return deleted_cnt


# Функция для удаления записей из базы по id
async def delete_record_from_db(record_id):
    await BTCPrice.filter(id=record_id).delete()


# Функция для обновления записей в базе
async def update_db(record_id, updated_data):
    try:
        record = await BTCPrice.filter(id=record_id).first()

        record.title = updated_data.get('title', record.title)
        record.price = updated_data.get('price', record.price)
        record.max_price = updated_data.get('max_price', record.max_price)
        record.min_price = updated_data.get('min_price', record.min_price)
        record.difference = updated_data.get('difference', record.difference)
        record.total_amount = updated_data.get('total_amount', record.total_amount)
        record.date = datetime.fromisoformat(updated_data.get('date', record.date))

        await record.save()
        return record
    except DoesNotExist:
        return None
