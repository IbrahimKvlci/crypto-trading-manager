from SpotExchangeBase import SpotExchangeBase
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.entities.User import User
    from app.entities.CryptocurrencyPair import CryptocurrencyPair

class SpotDemoExchange(SpotExchangeBase):
    def __init__(self):
        super().__init__()
    def get_balances(self, user:User):
        pass
    def buy_limit_order(self, user:User, cryptocurrency_pair:CryptocurrencyPair, price, quantity):
        pass
    def sell_limit_order(self, user:User, cryptocurrency_pair:CryptocurrencyPair, price, quantity):
        pass
    def buy_market_order(self, user:User, cryptocurrency_pair:CryptocurrencyPair, quantity):
        pass
    def sell_market_order(self, user:User, cryptocurrency_pair:CryptocurrencyPair, quantity):
        pass