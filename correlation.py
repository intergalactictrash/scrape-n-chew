import math

tvbl = [10,16,15,12,10,11,9,13,12,19]
pricel = [1400, 1404,1410,1402,1500,1502,1509,1511,1512,1519]

for i in range(0, len(tvbl)):
	avgtvb = sum(tvbl)/len(tvbl)
	avgprice = sum(pricel)/len(pricel)
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

c = rtop/denominator
print c