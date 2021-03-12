import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# Define Time Frame
now = dt.datetime.now()
start_year = now.replace(year = now.year - 1)
end_year = dt.datetime.now()

# Load Data
ticker_symbol = input('Ticker Symbol: ')
data = web.DataReader(ticker_symbol.upper(), 'yahoo', start_year, end_year)
print(data.columns)

# Restructure Data
data = data[['Open', 'High', 'Low', 'Close']]
data.reset_index(inplace=True)