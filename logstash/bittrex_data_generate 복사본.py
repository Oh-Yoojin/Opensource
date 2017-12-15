
import time
from bittrex import Bittrex
import pandas as pd

apikey = 'fd25ef6daf6c4d5cb8507878781df312'
secret = '5f00769f175141be861bf199f089f9fd'
my_bittrex = Bittrex(apikey, secret)
my_bittrex.get_currencies()
my_bittrex.get_marketsummary('BTC-LTC')

coinList = [{'CoinName': x['MarketCurrency'], 'CoinName_Full': x['MarketCurrencyLong'], 'MarketName': x['MarketName'],
             'BaseCurrency': x['BaseCurrency']} for x in my_bittrex.get_markets()['result']]
coinList = pd.DataFrame(coinList)
coinList

BTC-LTC,



col = ['MarketName', 'High', 'Low', 'Volume', 'Last', 'BaseVolume', 'TimeStamp', 'Bid', 'Ask', 'OpenBuyOrders', 'OpenSellOrders', 'PrevDay', 'Created']
market_price = pd.DataFrame(columns=col )
i = 0

while 1:
    market_price = pd.DataFrame(columns=col)
    time= time.asctime()
    for Market in coinList['MarketName'][0:10]:
        marketsummary = my_bittrex.get_marketsummary(Market)['result'][0]
        market_price = market_price.append((marketsummary), ignore_index=True)
    print(time)

    market_price.to_csv('bittrex_API_data.csv', sep=',')
    time.sleep(20)
    i += 1
    if i == 20:
        break

