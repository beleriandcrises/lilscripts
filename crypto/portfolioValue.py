# To print the total value of your portfolio, add your currencies and quantity like in the example


portfolio={'LTC': 1, 'XMR': 2, 'MIOTA': 3, 'ETH': 4, 'XLM': 5, 'XRP':6, 'EOS':7, 'NANO':8}

total=0.0

for pair in portfolio.items():
	cointick=dict(cmc.fetch_ticker(pair[0]+'/EUR'))
	cointick=cointick.get('info')
	coinPrice=cointick.get('price_eur')
	coinPrice=float(coinPrice)
	coinTotal=coinPrice*pair[1]
	total=total+coinTotal
	
print "Total value in EUR "+ str(round(total,2))
