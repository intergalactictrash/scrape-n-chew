#!/usr/bin/python

from lxml import html
import requests
from blockchain import statistics

sts = statistics.get()
print sts.mined_blocks

page = requests.get('https://coinmarketcap.com/')
tree = html.fromstring(page.content)

blockchain = requests.get('https://blockchain.info/stats')
stats = html.fromstring(blockchain.content)

bitcoinity = requests.get('https://data.bitcoinity.org/bitcoin/hashrate/6m?c=m&g=15&t=a')
mining = html.fromstring(bitcoinity.content)

reddit = requests.get('https://www.reddit.com/r/Bitcoin/new/')
users = html.fromstring(reddit.content)


btcprice = tree.xpath('//*[@id="id-bitcoin"]/td[7]')[0].text
print "btc change "+ btcprice
btcusd = tree.xpath('//*[@id="id-bitcoin"]/td[4]/a')[0].text
print "btc price "+ btcusd
btcvol = tree.xpath('//*[@id="id-bitcoin"]/td[6]/a')[0].text
print "btc volume (24hr): "+ btcvol
print type(btcvol)
btcblocksize = stats.xpath('//*[@id="minutes_between_blocks"]')[0].text
print "btc block size: ", btcblocksize
btcmining = mining.xpath('//*[@id="compare"]/div[2]/div[1]/table/tbody/tr[1]/td[2]/text()')#[0].text
print "antpool hashrate: " , btcmining
btcreddit = users.xpath('/html/body/div[3]/div[6]/div/p/span[1]/text()')#[0].text
print "readers on reddit: ", btcreddit



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