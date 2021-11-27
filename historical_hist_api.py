import config
import pandas as pd
from binance.client import Client
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

client = Client(config.API_KEY, config.API_SECRET)

def historical_hist_api_call(startyear):

    today = datetime.today() 
    yesterday = (today - timedelta(days=1))
    start_year = yesterday - relativedelta(years=startyear)
    end_year = yesterday - relativedelta(years=startyear-1)
    start_year = start_year.strftime("%d %b, %Y")
    end_year = end_year.strftime("%d %b, %Y")

    cryptos = {
        "bitcoin_usdt" : 'btcusdt',
        "ethereum_usdt" : 'ethusdt',
        "ada_usdt" : 'adausdt',
        "ripple_usdt" : 'xrpusdt',
        "solana_usdt" :'solusdt',
        "bitcoin_usd" : 'btcusd',
        "ethereum_usd" : 'ethusd',
        "ada_usd" : 'adausd',
        "ripple_usd" : 'xrpusd',
        "solana_usd" :'solusd'}

    db_dict = {}

    for crypto in cryptos:
        container = []
        coin = (cryptos[crypto]).upper()
        candles = client.get_historical_klines(coin, Client.KLINE_INTERVAL_1DAY, end_year, start_year)

        for candlestick in candles:
            container.append(candlestick)
        db_dict[crypto] = [container]

    # empty dataframe to hold values
    historical_df = pd.DataFrame(
        {"crypto": [],
        "time" : [],
        "open" : [],
        "high" : [],
        "low" : [],
        "close" : [],
        "volume" : [],
        "trade" : []
        }
    )

    # loop through each time on for each crypto and append to dataframe
    for crypto in cryptos:
        for time_interval in db_dict[crypto][0]:


            date_col = time_interval[0]/1000
            open_col = time_interval[1]
            high_col = time_interval[2]
            low_col = time_interval[3]
            close_col = time_interval[4]
            vol_col = time_interval[5]
            trade_col = time_interval[9]


            new_row = [{"crypto": crypto,
                    "time" : date_col,
                    "open" : open_col,
                    "high" : high_col,
                    "low" : low_col,
                    "close" : close_col,
                    "volume" : vol_col,
                    "trade" : trade_col
                    }]

            historical_df = historical_df.append(new_row,ignore_index=True,sort=False)

    return(historical_df)


def shortinterval_api_call():

    today = datetime.today() 
    yesterday = today - relativedelta(days=1)
    today = today.strftime("%d %b, %Y")
    yesterday = yesterday.strftime("%d %b, %Y")

    now = datetime.now(tz=None).timestamp()
    print(now)

    cryptos = {
        "bitcoin_gbp" : 'btcgbp',
        "ethereum_gbp" : 'ethgbp',
        "ada_gbp" : 'adagbp',
        "ripple_gbp" : 'xrpgbp',
        "solana_gbp" :'solgbp'}

    db_dict = {}

    for crypto in cryptos:
        container = []
        coin = (cryptos[crypto]).upper()
        candles = client.get_historical_klines(coin, Client.KLINE_INTERVAL_1MINUTE, yesterday)

        for candlestick in candles:
            container.append(candlestick)
        db_dict[crypto] = [container]

    # empty dataframe to hold values
    shortinterval_df = pd.DataFrame(
        {"crypto": [],
        "time" : [],
        "open" : [],
        "high" : [],
        "low" : [],
        "close" : [],
        "volume" : [],
        "trade" : []
        }
    )

    # loop through each time on for each crypto and append to dataframe
    for crypto in cryptos:
        for time_interval in db_dict[crypto][0]:


            date_col = time_interval[0]/1000
            open_col = time_interval[1]
            high_col = time_interval[2]
            low_col = time_interval[3]
            close_col = time_interval[4]
            vol_col = time_interval[5]
            trade_col = time_interval[9]


            new_row = [{"crypto": crypto,
                    "time" : date_col,
                    "open" : open_col,
                    "high" : high_col,
                    "low" : low_col,
                    "close" : close_col,
                    "volume" : vol_col,
                    "trade" : trade_col
                    }]

            shortinterval_df = shortinterval_df.append(new_row,ignore_index=True,sort=False)

    return(shortinterval_df)