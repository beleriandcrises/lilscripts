#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import ccxt


#Coin checking part

cmc=ccxt.coinmarketcap()
 

def getPrice(coin):
	cointick=dict(cmc.fetch_ticker(coin+'/EUR'))
	cointick=cointick.get('info')
	coinPrice=cointick.get('price_eur')
	coinPrice=float(coinPrice)
	return coinPrice
		
LTC = getPrice('LTC')

XLM = getPrice('XLM')

TotalLTC= LTC*19.442

getBack=TotalLTC/XLM

# Mail part

 
fromaddr = "alex.desirio@libero.it"
toaddr = "manuel.moscariello@24finance.it"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "con quello che hai ora puoi comprare " + str(getBack) + " XLM"
 
body = "forza, su"
msg.attach(MIMEText(body, 'plain'))


# Send emails

if getBack > 9000:
	server = smtplib.SMTP('smtp.libero.it', 587)
	server.starttls()
	server.login(fromaddr, "Carotina01.")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

