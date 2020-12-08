def rr(x,k,l):
	#print('Your k is ' + str(k) + '\n')
	#print('Your l is ' + str(l) + '\n')
	out = -x/(k**2+2*k*l+l**2+3*k+3*l) #Change to recursive relation
	return out

def cof(lower,upper,step,l):
	list=[1,0] #Change for first coefficient depending on choice of lambda
	x = 1
	a = var('a')
	for n in range(lower,upper+1,step):
		a = simplify(expand(rr(x,n,l)))
		x = a
		list.append(a)
		list.append(0)
	return list
	
def diffcof(list):
	out = []
	for cof in list:
		a = diff(cof)
		out.append(a)
	return out
	
