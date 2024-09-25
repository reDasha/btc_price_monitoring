import csv

CSV_FILE = 'btc_prices.csv'

# Функция для записи в файл .csv
async def save_to_csv(title, price, max_price, min_price, date, difference, total_amount):
    header = ['title', 'price', 'max price', 'min price', 'date ISOformat', 'difference', 'total amount']

    file_exists = False
    try:
        with open(CSV_FILE, 'r'):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(header)

        writer.writerow([title, price, max_price, min_price, date, difference, total_amount])