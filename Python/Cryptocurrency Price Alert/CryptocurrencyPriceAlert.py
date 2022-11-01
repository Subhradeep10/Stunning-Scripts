# A python script that alerts you by opening your portfolio webpage on browser when a cryptocurrency hits a certain price.

'''
Example: If MATIC hits $0.80 or more, it will automatically open a webpage (crypto trade) on the user's browser.

(it will run in background using cronjob)

Use case: Crypto prices are highly volatile and there are no stop loss or good alert systems in many exchange platforms. This will help the user to stay updated with the crypto price trend while they do other tasks.
'''

# cryptocompare is a library that fetches the cryptocurrency prices
# more details about the library: https://pypi.org/project/cryptocompare/
# you can install it using: pip install cryptocompare

from cryptocompare import get_price as gp

# webbrowser opens the default webbrowser of the system
from webbrowser import open as op

# define prices
# get_price returns
# {'SYMBOL': {'USD': 1.000}}
# nested [foo][bar] to get value in float

# note: only use what you need, comment rest, this will save time fetching the prices

BTC = gp('BTC', currency='USD')['BTC']['USD']
MATIC = gp('MATIC', currency='USD')['MATIC']['USD']
# ETH = gp('ETH', currency='USD')['ETH']['USD']
# ADA = gp('ADA', currency='USD')['ADA']['USD']
# SOL = gp('SOL', currency='USD')['SOL']['USD']
# XRP = gp('XRP', currency='USD')['XRP']['USD']
# CRO = gp('CRO', currency='USD')['CRO']['USD']
# DOT = gp('DOT', currency='USD')['DOT']['USD']
# XLM = gp('XLM', currency='USD')['XLM']['USD']
# SHIB = gp('SHIB', currency='USD')['SHIB']['USD']
# ALGO = gp('ALGO', currency='USD')['ALGO']['USD']
# NEAR = gp('NEAR', currency='USD')['NEAR']['USD']
# ATOM = gp('ATOM', currency='USD')['ATOM']['USD']


# retrieve prices and compare
# if the condition satisfies, use the webbrowser module to open relevant links

if MATIC <= 1.42:
    # this will open the chart page on coinmarketcap
    op('https://coinmarketcap.com/currencies/polygon/')

    # this opens the page to your cryptocurrency exchange platform 
    op('https://coindcx.com/insta/buy/matic')

#if BTC >= 45000.0:
#    op('https://coinmarketcap.com/currencies/bitcoin/')
#    op('https://coindcx.com/insta/sell/btc')

# use this script in cronjob
# crontab -e
# * * * * * python3 /home/username/path/to/cryptalert.py

# After you add this to cronjob, this script will run every minute
# You can change this using https://crontab-generator.org/