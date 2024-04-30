"""Module to get the configuration to be used by the bot."""

import json
import os
from pathlib import Path


def ask_config_file():
    """Function to ask for the configuration file."""
    json_name = "config.json"
    # json_name = input(
    #     "Introduzca el nombre completo del archivo de configuración:")
    file = Path(f"./config_files/{json_name}")
    return file


def load_config_data(file):
    """Function to load all the configuration parameters from the file."""
    try:
        with open(file, "r", encoding="UTF-8") as current_json_file:
            json_data = current_json_file.read()
        config_data = json.loads(json_data)
        return config_data
    except FileNotFoundError as ex:
        print(ex)
        print("Archivo de configuración no encontrado.")


def get_config():
    """Function to get all the configuration data."""
    json_file = ask_config_file()
    config_data = load_config_data(json_file)
    configuration = Configuration(config_data)
    return configuration


class Configuration():
    """Class representing every configuration parameter"""

    def __init__(self, config_data):
        self.url = config_data["url"]
        self.searched_coins = config_data["criptomonedas"]
        self.hora = config_data["programacion"]["hora"]
        self.sender_email = os.environ.get("SENDGRID_EMAIL")
        self.apikey = os.environ.get("SENDGRID_API_KEY")
        self.recipients = config_data["correo"]["destinatario"]
