def power_series_gen( degree,center,constant ):
	x,out = var('x','out')
	out = constant * (x - center)^degree
	return str(out)
	
def power_series(lower,upper):
	i = 0
	for n in constants_range(lower,upper):
		a = power_series_gen(i,2,n)
		if i < upper:
			print a + "+"
		else:
			print a
		i = i + 1
		

def ps(list):
	i = 0
	for coef in list:
		a = power_series_gen(i,0,coef)
		if i < 6:
			print a + "+"
		else:
			print a
		i = i + 1