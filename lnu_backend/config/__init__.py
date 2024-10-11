import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'config', 'config.ini'))

# Data Base
HOST = config.get('my_service', 'host')
USER = config.get('my_service', 'user')
DB_NAME = config.get('my_service', 'dbname')
PASSWORD = config.get('my_service', 'password')
PORT = config.get('my_service', 'port')
