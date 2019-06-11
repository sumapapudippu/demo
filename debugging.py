import ipdb

def transform(x,y):
	y = y**2
	x *= 2
	z = x+y
	return z
x=50
y=60
z=5
n1=1000
ipdb.set_trace()
transform(5,10)
print('z='+str(z))
n1 = transform(2,3)
print('n='+str(n1))	



