from __future__ import division
import math
from tabulate import tabulate

i = 0
out = []

for n in range(1,100):
	i = 1/n**2 + i
	row = [i,n]
	out.append(row)
	
print tabulate(row,headers=["i","n"],tablefmt="grid")