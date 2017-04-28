#!/usr/bin/python

from lxml import html
import requests
from time import *
from blockchain import statistics

sts = statistics.get()
mine=sts.mined_blocks
print "mined blocks: ", mine
tvb=sts.trade_volume_btc 
print "trade vlovume (btc): ", tvb
minerrevusd=sts.miners_revenue_usd 
print "Miner revenue (usd): ", minerrevusd
btcmine=sts.btc_mined
print "btc mined: ", btcmine
tvusd=sts.trade_volume_usd
print "volume traded (usd): ", tvusd 
diff=sts.difficulty
print "difficulty: ", diff
blocktime=sts.minutes_between_blocks
print "minutes between blocks: ", blocktime 
transnum=sts.number_of_transactions
print "number of transactions: ", transnum 
hashrate=sts.hash_rate
print "hashrate: ", hashrate
time=sts.timestamp
print "timestamp: ", time
blockmine=sts.mined_blocks
print "blocks mined: ", blockmine
blocksize=sts.blocks_size
print "bocksize: ", blocksize
fees=sts.total_fees_btc
print "total fees (btc): ", fees
btcsent=sts.total_btc_sent
print "total sent btc: ", btcsent
estbtcsent=sts.estimated_btc_sent 
print "estemated sent btc: ", estbtcsent
totbtc=sts.total_btc 
print "btc in circulation: ", totbtc
totblocks=sts.total_blocks
print "total number of blocks: ", totblocks
retarg=sts.next_retarget
print  "next retarget: ", retarg
volusd=sts.estimated_transaction_volume_usd
print "estimated transaction volume (usd): ", volusd
minerrevbtc=sts.miners_revenue_btc  
print "miner revenue (btc): ", minerrevbtc
price=sts.market_price_usd 
print "btc price (usd): ", price


tvbl = []
pricel = []
for i in range(0, 3):
	tvbl.append(tvb)
	pricel.append(price)
	avgtvb = sum(tvbl)/len(tvbl)
	avgprice = sum(pricel)/len(pricel)
	sleep(2)
print tvbl
print "average", avgtvb


for i in range(0, len(tvbl)):
	x = tvbl[i] - avgtvb
	y = pricel[i] - avgprice
print x
print y







