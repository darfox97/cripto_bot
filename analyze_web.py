"""Module providing functions to scrap a crypto website and obtain cryptocurrency data."""

import requests
from bs4 import BeautifulSoup
# from coin import Coin


def get_soup(url, ext_url=""):
    """Function obtaining the main HTML soup of a website."""
    response = requests.get(url+ext_url, timeout=10)
    html_text = response.text
    soup = BeautifulSoup(html_text, "html.parser")
    return soup


def get_searched_coin_data(coin, index_soup, config):
    """Function to get the main Coin class atributes."""
    coin_link = get_coin_link(coin, index_soup)
    # Obtener la soup de la cripto seleccionada:
    searched_cripto_soup = get_soup(config.url, coin_link)
    coin_name = coin
    coin_initials = get_coin_initials(searched_cripto_soup)
    coin_price = get_coin_price(searched_cripto_soup)
    # Creamos objeto Coin con los datos de la criptomoneda actual:
    current_coin = Coin(coin_name, coin_link, coin_initials, coin_price)

    return current_coin


# Obtener las iniciales de una cripto a partir de su soup:
def get_coin_initials(soup):
    """Function to get the initials of a criptocurrency."""
    coin_h1 = soup.find("h1")
    coin_initials = coin_h1.find("span").text.split()[0]
    return coin_initials


# Obtener el precio de una cripto a partir de su soup:
def get_coin_price(soup):
    """Function to get the price of a criptocurrency."""
    coin_price_str = soup.find(
        "span", {"data-converter-target": "price"}).text
    coin_price = coin_price_str.replace("$", "")
    coin_price = coin_price.replace(",", "")
    return coin_price


def get_coin_link(coin_name, index_soup):
    """Function to get the url link of a criptocurrency."""
    links = index_soup.find_all(
        "a", href=lambda href: href and coin_name.lower() in href)
    link = links[0]["href"]
    return link


def get_all_coin_data(config):
    """Main Function to get the data of all the searched cryptos."""
    # Obtenemos la soup inicial de la web:
    index_soup = get_soup(config.url)
    # Obtenemos los datos de cada moneda especificada en la configuración:
    coin_data = []
    for searched_coin in config.searched_coins:
        coin_object = get_searched_coin_data(searched_coin, index_soup, config)
        coin_data.append(coin_object)

    return coin_data


class Coin():
    """Class representing the main values of a cyptocurrency."""

    def __init__(self, name, link, initials, price):
        self.name = name
        self.initials = initials
        self.price = price
        self.link = link
