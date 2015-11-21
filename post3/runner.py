"""
The main file that will evolve into our trading library
"""
from datetime import datetime
import oandapy

OANDA_ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
OANDA_ACCOUNT_ID = 11111 #put your access id here 

def main():
    print "------ System online -------", datetime.now()
    oanda = oandapy.API(environment="practice",
                        access_token=OANDA_ACCESS_TOKEN)
    response = oanda.get_prices(instruments="EUR_USD")
    prices = response.get("prices")
    buy_price = prices[0].get("bid")

    print "Buy at", buy_price
    
    trade_id = oanda.create_order(OANDA_ACCOUNT_ID, instrument="EUR_USD",
                                  units=100000,
                                  side='buy',
                                  type='market')

    print "Trading id", trade_id


if __name__ == "__main__":
    main()
