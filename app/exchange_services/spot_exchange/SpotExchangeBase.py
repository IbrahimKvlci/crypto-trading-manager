from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.entities.User import User
    from app.entities.CryptocurrencyPair import CryptocurrencyPair


class SpotExchangeBase:
    def __init__(self):
        pass
    def get_balances(self, user:User):
        raise NotImplementedError("Subclass must implement this method") 
    def buy_limit_order(self, user:User, cryptocurrency_pair:CryptocurrencyPair, price, quantity):
        raise NotImplementedError("Subclass must implement this method")
    def sell_limit_order(self, user:User, cryptocurrency_pair:CryptocurrencyPair, price, quantity):
        raise NotImplementedError("Subclass must implement this method")
    def buy_market_order(self, user:User, cryptocurrency_pair:CryptocurrencyPair, quantity):
        raise NotImplementedError("Subclass must implement this method")
    def sell_market_order(self, user:User, cryptocurrency_pair:CryptocurrencyPair, quantity):
        raise NotImplementedError("Subclass must implement this method")