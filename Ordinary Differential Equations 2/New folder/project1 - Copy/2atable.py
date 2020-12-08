#create table for air resistance models
from __future__ import division
import math
from tabulate import tabulate

time = [0,2,4,6,8,10,100,150,200,250,1000]
kl = 1
kq = .01
g = 9.815
m = 1000
vnr = 0
vlm = m*g/kl
vlq = 0
out = []
out2 = []
variables = [m,g,kl,kq]
##print "Time\t |No Resistance\t |Linear Model\t |Quadratic Model\n"
for t in time:
	nr = g*t + vnr
	##lm = (m*g/kl) + (vlm*math.exp(-kl*t/m))/(m*g)
	lq = math.sqrt(m*g/kq)*(-1-((vlq*math.sqrt(kq)+math.sqrt(m*g))/(vlq - math.sqrt(m*g))*math.exp((2*g*math.sqrt(kq)*t)/(math.sqrt(m*g)))))/(1-((vlq*math.sqrt(kq)+math.sqrt(m*g))/(vlq - math.sqrt(m*g))*math.exp((2*g*math.sqrt(kq)*t)/(math.sqrt(m*g)))))
	lm = (vlm)*((1.0-math.exp((-kl*t/m))))
	##lm = (vlm)*((abs(math.expm1((-kl*t/m)))))
	##print vlm
	##vnr = 1
	##vlm = 0
	##vlq = 0
	row = [t,nr,lm,lq]
	out.append(row)
##	print t,'\t |',nr,'\t |',lm,'\t |',lq,'\n'
row = ["inf","inf",(m*g/kl),(math.sqrt(m*g/kq))]
out.append(row)
out2.append(variables)
print tabulate(out,headers=["Time","No Resistance","Linear Model","Quadratic Model"],tablefmt="grid")
print "\n"
print tabulate(out2,headers=["Mass","Gravity","K Linear","K Quadratic"],tablefmt="grid")