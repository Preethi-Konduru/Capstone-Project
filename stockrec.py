import nsepy  # to extract historical and real time data from NSE
import csv
from datetime import datetime
from datetime import date
from nsepy import get_history
import pandas as pd
import numpy as np
import plotly.graph_objects as go

pd.options.display.max_columns = None
pd.options.display.max_rows = None


def get_price_data_NSE(stock):
    try:
        stock_data = get_history(symbol=stock,
                                 start=date(2022, 1, 1),
                                 end=date(2023, 2, 3))
        ##        data = NSEpy.get_history(symbol=stock, start=NSEpy.get_date(days_ago=365), end=NSEpy.get_date(0))

        print("Fetching data for stock:", stock)
        df = pd.DataFrame(stock_data)
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        df['SMA_150'] = df['Close'].rolling(window=150).mean()
        df['SMA_200'] = df['Close'].rolling(window=200).mean()
        df['Position'] = np.where(df['SMA_50'] > df['SMA_200'], 'Buy', 'Sell')

        # Storing required values
        currentClose = df["Close"][-1]
        moving_average_50 = df["SMA_50"][-1]
        moving_average_150 = df["SMA_150"][-1]
        moving_average_200 = df["SMA_200"][-1]
        low_of_52week = round(min(df["Low"][-260:]), 2)
        high_of_52week = round(max(df["High"][-260:]), 2)
        print("currentClose:", currentClose, "\n",
              "Moving Average 50:", moving_average_50, "\n",
              "Moving Average 150", moving_average_150, "\n",
              "Moving Average 200:", moving_average_200, "\n",
              "52 week Low:", low_of_52week, "\n",
              "52 week High", high_of_52week, "\n", )
        global df_n
        df_n = pd.DataFrame(df)
        print(df_n)
        try:
            moving_average_200_20 = df["SMA_200"][-20]
        except Exception:
            moving_average_200_20 = 0

        # Condition 1: Current Price > 150 SMA and > 200 SMA
        condition_1 = currentClose > moving_average_150 > moving_average_200

        # Condition 2: 150 SMA and > 200 SMA
        condition_2 = moving_average_150 > moving_average_200

        # Condition 3: 200 SMA trending up for at least 1 month
        condition_3 = moving_average_200 > moving_average_200_20

        # Condition 4: 50 SMA> 150 SMA and 50 SMA> 200 SMA
        condition_4 = moving_average_50 > moving_average_150 > moving_average_200

        # Condition 5: Current Price > 50 SMA
        condition_5 = currentClose > moving_average_50

        # Condition 6: Current Price is at least 30% above 52 week low
        condition_6 = currentClose >= (1.3 * low_of_52week)

        # Condition 7: Current Price is within 25% of 52 week high
        condition_7 = currentClose >= (.75 * high_of_52week)

        if (
                condition_1 and condition_2 and condition_3 and condition_4 and condition_5 and condition_6 and condition_7):
            return "BUY"

    except Exception as e:
        print(e)
        print(f"Could not gather data on {stock}")


def get_candlestick(u_stock):
    figure = go.Figure(data=[go.Candlestick(x=df_n.index,
                                            open=df_n["Open"],
                                            high=df_n["High"],
                                            low=df_n["Low"],
                                            close=df_n["Close"])])
    figure.update_layout(title="Stock Price Analysis for " + u_stock.upper(),
                         xaxis_rangeslider_visible=False)
    figure.show()


u_stock = input("Enter the stock name you want to analyse:")
print("You can BUY" if (
            get_price_data_NSE(u_stock) == "BUY") else "Not a good time to invest, may be time to consider to sell")
print(get_candlestick(u_stock) if input(
    "Do you want to check the candlestick for the stock?confirm Y/N:") == "Y" else "bye")