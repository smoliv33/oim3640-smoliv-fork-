# in Command prompt, "python -m pip install yfinance"
import yfinance as yf
import pprint


tsla = yf.Ticker('TSLA') # a Ticker instance (OOP)

# pprint.pprint(tsla.info)
print(type(tsla.info))

print(tsla.info['currentPrice'])