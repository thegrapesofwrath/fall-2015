import math as m
from tabulate import tabulate as t
import matplotlib.pyplot as plt
import pylab as pl



start = 1
stop = 50
step = 1
power = 3
function = "1/n^2"
out = []
x_list = []
y_list = []
y_last = 0


 
for i in range(start,stop+1,step):
		#print i
		y = y_last + 1/m.pow(i,power)
		y_list.append(y)
		x_list.append(i)
		#print y
		y_last = y
		row = [i,y]
		out.append(row)
print t(out,headers=["x","y"],tablefmt="grid")
plt.plot(x_list,y_list)
plt.show()