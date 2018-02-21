#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# requires ccxt.
# More infos on https://github.com/ccxt/ccxt

# To put it in your conky place the script somewhere, chmod +x and in your conky file put a line like this
# ${font Monospace:normal:size=8}${color1}${texeci 300 python /path/to/your/script/conkymarketcap.py}


import ccxt

cmc=ccxt.coinmarketcap()


# Write here the coins you want to fetch the price for, in single quotes separated by a comma
# Some tickers in coinmarketcap can be unpredictable, like 'MIOTA' for iota. If it doesn't work check your ticker for coinmarketcap online
# The coins will appear on the list in the order you put them

coins=['ETH','LTC', 'XLM', 'XMR', 'XRP', 'EOS', 'MIOTA', 'BTC','NANO']

for coin in coins:
	cointick=dict(cmc.fetch_ticker(coin+'/EUR'))
	cointick=cointick.get('info')
	coinPrice=cointick.get('price_eur')
	coinWeek=cointick.get('percent_change_7d')
	coinDay=cointick.get('percent_change_24h')
	coinHour=cointick.get('percent_change_1h')
	print(coin +" "+str(round(float(coinPrice),3))+"\nW("+coinWeek+") D("+coinDay+") H("+coinHour+")\n")
	

