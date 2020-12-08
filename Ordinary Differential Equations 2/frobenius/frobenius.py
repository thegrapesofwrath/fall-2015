R.<x,l,k> = PolynomialRing(RR)
lower = 0
upper = 5
l = var('l')
f0 = x**l
f1 = diff(f0,x)
f2 = diff(f1,x)

def get_function():
	function = input("Please enter a function\nPlease use ** for exponentiation\nPlease use a . after any divisors to avoid integer division\n")
	return function

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
	return str(latex(out))

def power_series(lower,upper):
	i = 0
	for n in constants_range(lower,upper):
		a = power_series_gen(i,2,n)
		if i < upper:
			print a + "+"
		else:
			print a
		i = i + 1
		

def equalize_degrees(coefficient,function):
	if str(function)[-1] == ')':
	
	else:
	
	
	
	
	
	
	var(str(f0)[-1]) + int(str(f1)[-4:-1])
	