#!/usr/bin/env python
# -*- coding: utf-8 -*-
# requires ccxt. To install on debian:
#sudo pip install ccxt
#
# If you don't have pip install with with:
#sudo apt-get install python-pip
#
# More infos on https://github.com/ccxt/ccxt

# To put it in your conky place the script somewhere, chmod +x and in your conky file put a line like this
# ${font Monospace:normal:size=8}${color1}${texeci 300 python /path/to/your/script/coinmarketcap.py}


import ccxt

cmc=ccxt.coinmarketcap()


# Write here the coins you want to fetch the price for, in single quotes separated by a comma
# Some tickers in coinmarketcap can be unpredictable, like 'MIOTA' for iota. If it doesn't work check your ticker for coinmarketcap online
# The coins will appear on the list in the order you put them

coins=['ETH','LTC', 'XLM', 'XMR', 'XRP', 'EOS', 'REQ', 'BCH', 'MIOTA']

for coin in coins:
	cointick=dict(cmc.fetch_ticker(coin+'/EUR'))
	cointick=cointick.get('info')
	coinPrice=cointick.get('price_eur')
	coinWeek=cointick.get('percent_change_7d')
	coinDay=cointick.get('percent_change_24h')
	coinHour=cointick.get('percent_change_1h')
	print(coin +" "+coinPrice+"\nW("+coinWeek+") D("+coinDay+") H("+coinHour+")\n")
	
print("\n\n")
# To print the total value of your portfolio, add your currencies and quantity like in the example


portfolio={'LTC': 9, 'XMR': 3, 'MIOTA': 402, 'BCH': 0.46, 'ETH':8, 'XLM':9500, 'XRP':805, 'EOS':530}

total=0.0

for pair in portfolio.items():
	cointick=dict(cmc.fetch_ticker(pair[0]+'/EUR'))
	cointick=cointick.get('info')
	coinPrice=cointick.get('price_eur')
	coinPrice=float(coinPrice)
	coinTotal=coinPrice*pair[1]
	total=total+coinTotal
	
print "The total value of your portfolio in EUR is "+ str(total)










