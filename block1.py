#!/usr/bin/python

from lxml import html
import requests
from time import *
from blockchain import statistics
import math


sts = statistics.get()

mine = sts.mined_blocks
tvb = sts.trade_volume_btc 
minerrevusd = sts.miners_revenue_usd 
btcmine = sts.btc_mined
tvusd = sts.trade_volume_usd
diff = sts.difficulty
blocktime = sts.minutes_between_blocks
transnum = sts.number_of_transactions
hashrate = sts.hash_rate
time = sts.timestamp
blockmine = sts.mined_blocks
blocksize = sts.blocks_size
fees = sts.total_fees_btc
btcsent = sts.total_btc_sent
estbtcsent = sts.estimated_btc_sent 
totbtc = sts.total_btc 
totblocks = sts.total_blocks
retarg = sts.next_retarget
volusd = sts.estimated_transaction_volume_usd
minerrevbtc = sts.miners_revenue_btc  
price = sts.market_price_usd 
print "btc price (usd): ", price
print "mined blocks: ", mine
print "trade vlovume (btc): ", tvb
print "Miner revenue (usd): ", minerrevusd
print "btc mined: ", btcmine
print "volume traded (usd): ", tvusd 
print "difficulty: ", diff
print "minutes between blocks: ", blocktime 
print "number of transactions: ", transnum 
print "hashrate: ", hashrate
print "timestamp: ", time
print "blocks mined: ", blockmine
print "bocksize: ", blocksize
print "total fees (btc): ", fees
print "total sent btc: ", btcsent
print "estemated sent btc: ", estbtcsent
print "btc in circulation: ", totbtc
print "total number of blocks: ", totblocks
print  "next retarget: ", retarg
print "estimated transaction volume (usd): ", volusd
print "miner revenue (btc): ", minerrevbtc


tvbl = []
pricel = []
minel = []
minerrevusdl =[]
btcminel = []
tvusdl = []
diffl = []
blocktimel = []
transnuml = []
hashratel = []
timel = []
blockminel =[]
blocksizel = []
feesl = []
btcsentl = []
estbtcsentl = []
totbtcl = []
totblocksl = []
retargl = []
volusdl = []
minerrevbtcl = []


for i in range(0, 3):
	tvbl.append(tvb)
	minel.append(mine)
	minerrevusdl.append(minerrevusd)
	btcminel.append(btcmine)
	diffl.append(diff)
	blocktimel.append(blocktime)
	transnuml.append(transnum)
	hashratel.append(hashrate)
	timel.append(time)
	blockminel.append(blockmine)
	feesl.append(fees)
	btcsentl.append(btcsent)
	estbtcsentl.append(estbtcsent)
	totbtcl.append(totbtc)
	totblocksl.append(totblocks)
	retargl.append(retarg)
	volusdl.append(volusd)
	minerrevbtcl.append(minerrevbtc)

	pricel.append(price)
	avgtvb = sum(tvbl)/len(tvbl)
	avgmine = sum(minel)/len(tvbl)
	avgminerrevusd = sum(minerrevusdl)/len(tvbl)
	avgbtcmine = sum(btcminel)/len(tvbl)
	avgdiff = sum(diffl)/len(tvbl)
	avgblocktime = sum(blocktimel)/len(tvbl)
	avgtransnum = sum(transnuml)/len(tvbl)
	avghashrate = sum(hashratel)/len(tvbl)
	avgtime = sum(timel)/len(tvbl)
	avgblockmine = sum(blockminel)/len(tvbl)
	avgfees = sum(feesl)/len(tvbl)
	avgbtcsent = sum(btcsentl)/len(tvbl)
	avgestbtcsent = sum(estbtcsentl)/len(tvbl)
	avgtotbtc = sum(totbtcl)/len(tvbl)
	avgtotblocks = sum(totblocksl)/len(tvbl)
	avgretarg = sum(retargl)/len(tvbl)
	avgvolusd = sum(volusdl)/len(tvbl)
	avgminerrevbtc = sum(minerrevbtcl)/len(tvbl)

	avgprice = sum(pricel)/len(pricel)
	sleep(2)
print tvbl
print "average", avgtvb

sqxtvbl = []
sqyl = []
numeratorl = []
for i in range(0, len(tvbl)):
	xtvb = tvbl[i] - avgtvb
	print xtvb
	y = pricel[i] - avgprice
	print y
	sqxtvb = xtvb**2
	sqxtvbl.append(sqxtvb)
	sqy = y**2
	sqyl.append(sqy)
	numerator = xtvb * y
	numeratorl.append(numerator)
	print "numerator of 'r': ", numerator
print "out: ", xtvb
print "out: ", y
rtop = sum(numeratorl)
print "numberator after summation: ", rtop
denominator = math.sqrt(sum(sqxtvbl)) * math.sqrt(sum(sqyl))
print "denominator: ", denominator

#correlation = rtop/denominator
