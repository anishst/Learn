# SEE THIS FOR USAGE INFO: https://github.com/ranaroussi/yfinance
# resources
# https://medium.com/@ishan.s_54240/stock-data-and-analysis-529aa9aee60
# https://towardsdatascience.com/best-5-free-stock-market-apis-in-2019-ad91dddec984
import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
print(msft.info)

# show financials
print(msft.balance_sheet)

# show actions (dividends, splits)
print(msft.actions)

# get historical market data, here max is 5 years.
print(msft.history(period="max"))

df = msft.history(period="max")
print(df.describe())
print(df.tail(100))

import matplotlib.pyplot as plt

# Import the yfinance. If you get module not found error the run !pip install yfiannce from your Jupyter notebook
import yfinance as yf

# Get the data of the stock AAPL
data = yf.download('vfinx BAH msft', '2018-01-01', '2020-01-03')
# Plot the close price of the AAPL
print(data)
data.Close.plot()
plt.show()