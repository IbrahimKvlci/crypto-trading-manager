import configparser
from dotenv import load_dotenv
import os

load_dotenv()
config=configparser.ConfigParser()
config.read('config.ini')
enable_test=config.get('app','enable_test')
binance_base_url=config.get('binance_api','binance_base_url')

def get_binance_api_key():
    if enable_test:
        return os.getenv('BINANCE_TEST_API_KEY')
    return None #return user's api key
def get_binance_api_secret():
    if enable_test:
        return os.getenv('BINANCE_TEST_API_SECRET')
    return None #return user's api secret key
def get_binance_base_url():
    return binance_base_url
