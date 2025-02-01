from binance.spot import Spot
from binance.error import ClientError
import logging

def new_order(symbol,side,type,quantity,price,api_key,api_secret,base_url):
    client = Spot(api_key=api_key, api_secret=api_secret, base_url=base_url)
    params={
        "symbol": symbol,
        "side": side,
        "type": type,
        "timeInForce": "GTC",
        "quantity": quantity,
        "price": price,
    }
    try:
        response = client.new_order(**params)
        logging.info(response)
    except ClientError as error:
        logging.error("Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        ))
        return False
    return True