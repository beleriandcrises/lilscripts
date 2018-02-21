#!/usr/bin/env python

import ccxt

cmc=ccxt.coinmarketcap()

portfolio={'LTC': 9, 'XMR': 3, 'MIOTA': 402, 'ETH':8.849, 'XLM':10450, 'XRP':805, 'EOS':538, 'XRB':51}

total=0.0




for pair in portfolio.items():
	cointick=dict(cmc.fetch_ticker(pair[0]+'/EUR'))
	cointick=cointick.get('info')
	coinPrice=cointick.get('price_eur')
	coinPrice=float(coinPrice)
	coinTotal=coinPrice*pair[1]
	total=total+coinTotal

for pair in portfolio.items():
	cointick=dict(cmc.fetch_ticker(pair[0]+'/EUR'))
	cointick=cointick.get('info')
	coinPrice=cointick.get('price_eur')
	coinPrice=float(coinPrice)
	coinTotal=coinPrice*pair[1]
	coinTotal=round(coinTotal,2)
	perc=coinTotal*100/total
	perc=round(perc,2)
	print pair[0] + " " + str(perc)+" %"
