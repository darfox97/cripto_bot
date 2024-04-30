from datetime import datetime, timedelta
import csv


def read_csv():
    with open('prices.csv', encoding="UTF-8") as csv_file:
        data = csv.reader(csv_file, delimiter=";")
        rows = list(data)

    return rows


def get_yesterday_date():
    today_local = datetime.now()
    # Resta un día para obtener la fecha anterior
    yesterday_local = today_local - timedelta(days=1)
    # Obtiene solo el día de la fecha anterior
    yesterday = f"{
        yesterday_local.day}/{yesterday_local.month}/{yesterday_local.year}"
    return yesterday


def get_today_date():
    today_local = datetime.now()
    # Obtiene solo el día de la fecha anterior
    today = f"{
        today_local.day}/{today_local.month}/{today_local.year}"
    return today


def get_previous_price(rows, crypto):
    max_row = len(rows)
    # Comprobar que funciona aunque no haya precio previo sin esta línea:
    # previous_price = 0
    if max_row > 1:
        for i in range(max_row):
            date = rows[i][0]
            if date == get_yesterday_date() and rows[i][1] == crypto:
                previous_price = float(rows[i][3])
                return previous_price


def get_price_variation(previous_price, new_price):
    price_variation = ((new_price-previous_price)/previous_price)*100
    price_variation = round(price_variation, 2)
    return price_variation


def write_csv(rows, coin_data):
    updated_coins = []
    for coin in coin_data:
        crypto_name = coin.name
        initials = coin.initials
        price = float(coin.price)
        current_date = get_today_date()
        previous_price = get_previous_price(rows, crypto_name)
        price_variation = get_price_variation(previous_price, price)

        new_row = [current_date, crypto_name, initials, price, price_variation]
        updated_coins.append(new_row)
        rows.append(new_row)
        with open('prices.csv', 'w', newline='', encoding="UTF-8") as csv_file:
            writer = csv.writer(csv_file, delimiter=";")
            writer.writerows(rows)
    return updated_coins
