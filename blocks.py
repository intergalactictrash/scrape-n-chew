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

class correlation:

	def __init__(self, v, vlist):
		self.v = v
		self.vlist = []
		self.sqxvlist = []

	def average(self):
		for i in range(0, 3):
			self.vlist.append(self.v)
			pricel.append(price)
			avgv = sum(self.vlist)/len(self.vlist)
			avgprice = sum(pricel)/len(pricel)
			sleep(2)
		print self.vlist
		print "average", avgv
		self.avgv = avgv
		self.avgprice = avgprice
		return avgv
		return avgprice

	def formula(self):
		self.sqyl = []
		self.numeratorl = []
		for i in range(0, len(self.vlist)):
			self.xv = self.vlist[i] - self.avgv
			print self.xv
			self.y = pricel[i] - self.avgprice
			print self.y
			self.sqxv = self.xv**2
			self.sqxvlist.append(self.sqxv)
			self.sqy = self.y**2
			self.sqyl.append(self.sqy)
			self.numerator = self.xv * self.y
			self.numeratorl.append(self.numerator)
			print "numerator of 'r': ", self.numerator
		print "out: ", self.xv
		print "out: ", self.y
		self.rtop = sum(self.numeratorl)
		print "numberator after summation: ", self.rtop
		self.denominator = math.sqrt(sum(self.sqxvlist)) * math.sqrt(sum(self.sqyl))
		print "denominator: ", self.denominator

		#correlation = rtop/denominator

hh= correlation(tvb, tvbl)
hh.average()
hh.formula()


