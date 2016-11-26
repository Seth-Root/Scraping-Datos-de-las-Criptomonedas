# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-


import urllib2
from bs4 import BeautifulSoup
import re

Value_Euro_in_bolivar = 0
Value_Euro_in_bolivar = 0
value_BTC_dolares = 0

### Extracion de los Datos BTC
lista_monedas = ['bitcoin','steem','ethereum','ripple','litecoin','monero', 'dash', 'nem', 'dogecoin', 'waves']


for criptomoneda in lista_monedas:
                url = "https://coinmarketcap.com/currencies/" +criptomoneda
                page = urllib2.urlopen(url)
                soup = BeautifulSoup(page, "lxml")
                valor_btc = soup.find_all('span',class_="text-large" )
                
                for valores in valor_btc:
               
                               value_BTC_dolares = valores.get_text()
                               if value_BTC_dolares[0]=="$":
                                               value_BTC_dolares = value_BTC_dolares[1:]
                                               
                                               
                               elif value_BTC_dolares[-1]==")":
                                               continue
                                               
                               
                               value_BTC_dolares = float(value_BTC_dolares.replace(',','.'))
                               print 'El valor del  ', criptomoneda.upper() ,' se cotiza en: ', value_BTC_dolares , "Dolares"
   

                                
                



