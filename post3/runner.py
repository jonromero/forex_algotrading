"""
The main file that will evolve into our trading library
"""
from datetime import datetime, timedelta
import v20


OANDA_ACCESS_TOKEN = "01d4e6de4fc1246d2bfde02450871fe6-0ae159e87f2cc523a9116d9b535e85fa"
OANDA_ACCOUNT_ID = '101-001-6963280-001' #put your access id here 

def main():
    print("------ System online -------", datetime.now())
    latest_price_time = (datetime.utcnow() - timedelta(seconds=15)).isoformat('T')+'Z'

    api = v20.Context(
            'api-fxpractice.oanda.com',
            '443',
            token=OANDA_ACCESS_TOKEN)

    response = api.pricing.get(
                    OANDA_ACCOUNT_ID,
                    instruments='EUR_USD',
                    since=latest_price_time,
                    includeUnitsAvailable=False)

    print(response.reason + latest_price_time)
    
    prices = response.get("prices", 200)
    if len(prices):
        buy_price = prices[0].bids[0].price 

        print("Buy at" + str(buy_price))

        response = api.order.market(
            OANDA_ACCOUNT_ID,
            instrument='EUR_USD',
            units=5000)

        print("Trading id" + str(response.get('orderFillTransaction').id))
        print("Account Balance" + str(response.get('orderFillTransaction').accountBalance))
        print("Price" + str(response.get('orderFillTransaction').price))
        
    else:
        print(response.reason)

if __name__ == "__main__":
    main()
