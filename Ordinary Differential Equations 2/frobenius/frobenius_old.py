def constants_range( lower,upper ):
	list = var('list')
	list = []
	for n in range(lower,upper+1):
	    string = 'a' + str(n)
	    list.append(string)
    return list

def power_series_gen( degree,center,constant ):
	x,out = var('x','out')
	out = var(constant) * (x - center)^degree
	print latex(out)

	
i = 0
for n in constants_range(0,5):
    a = power_series_gen(i,2,n)
    i = i + 1