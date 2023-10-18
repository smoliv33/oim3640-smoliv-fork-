# in command prompt: "python -m pip install yfinance"

import yfinance as yf
import pprint

tsla = yf.Ticker('TSLA') # a Ticker instance (OOP)

# print(tsla.info)
# print(type(tsla.info))
# pprint.pprint(tsla.info)

tsla_info_dict = tsla.info
print(tsla_info_dict['currentPrice'])
