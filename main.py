"""Main module managing the flow of a bot which is run every day
to obtain the prices of specific cryptos, adding them to a CSV file,
comparing with previous days and sending the report by email."""

import gestion_config
import analyze_web
import csv_manager
import email_manager
# ¿Por qué funciona sin importar la clase Coin?
# from coin import Coin

# Obtiene un objeto Configuration con la configuración especificada en un archivo json:
configuration = gestion_config.get_config()

# Obtiene una lista de objetos Coin, que incluyen datos como el precio, mediante web scrapping:
coin_data = analyze_web.get_all_coin_data(configuration)

# Obtiene la lista de filas del fichero prices.csv:
prices_rows = csv_manager.read_csv()
# Añade los nuevos datos al CSV a partir de los anteriores, devolviendo los últimos datos actualizados:
updated_prices = csv_manager.write_csv(prices_rows, coin_data)
# Crea un objeto de tipo Mail con el cuerpo del mensaje:
message = email_manager.create_mail(updated_prices, configuration.recipients)
email_manager.send_email(message)
