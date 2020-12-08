def pde(equation,r,s,output):
	x = var('x')
	y = var('y')
	rx = var('rx')
	ry = var('ry')
	rxx = var('rxx')
	rxy = var('rxy')
	ryy = var('ryy')
	ux = var('ux')
	uy = var('uy')
	uxx = var('uxx')
	uxy = var('uxy')
	uyy = var('uyy')
	
	uxx = rx**2*urr + 2*rx*sx*urs + sx**2*uss + rxx*ur + sxx*us
	uxy = rx*ry*urr + (rx*sy + ry*sx)*urs + sx*sy*uss + rxy*ur + sxy*us
	uyy = ry**2*urr + 2*ry*sy*urs + sy**2*uss + ryy*ur + syy*us
	