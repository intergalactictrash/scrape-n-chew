#!/usr/bin/python

from lxml import html
import requests

page = requests.get('https://coinmarketcap.com/')
tree = html.fromstring(page.content)
btcprice = tree.xpath('//*[@id="id-bitcoin"]/td[7]')[0].text
print "btc change "+ btcprice
btcusd = tree.xpath('//*[@id="id-bitcoin"]/td[4]/a')[0].text
print "btc price "+ btcusd

ethprice = tree.xpath('//*[@id="id-ethereum"]/td[7]')[0].text
print "eth change "+ ethprice
ethusd = tree.xpath('//*[@id="id-ethereum"]/td[4]/a')[0].text
print "eth price "+ ethusd

xrpprice = tree.xpath('//*[@id="id-ripple"]/td[7]')[0].text
print "xrp change "+ xrpprice
xrpusd = tree.xpath('//*[@id="id-ripple"]/td[4]/a')[0].text
print "xrp price "+ xrpusd

xmrprice = tree.xpath('//*[@id="id-monero"]/td[7]')[0].text
print "xmr change "+ xmrprice
xmrusd = tree.xpath('//*[@id="id-monero"]/td[4]/a')[0].text
print "xmr price "+ xmrusd

dashprice = tree.xpath('//*[@id="id-dash"]/td[7]')[0].text
print "dash change "+ dashprice
dashusd = tree.xpath('//*[@id="id-dash"]/td[4]/a')[0].text
print "dash price "+ dashusd

ltcprice = tree.xpath('//*[@id="id-litecoin"]/td[7]')[0].text
print "ltc change "+ ltcprice
ltcusd = tree.xpath('//*[@id="id-litecoin"]/td[4]/a')[0].text
print "ltc price "+ ltcusd