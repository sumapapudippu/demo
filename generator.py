#generators : Generator fun generates sequence of values
def firstn(num):
	n=1
	while n <= num:
		yield n
		n=+1
values = firstnum(5)
next(values)
next(values)		
#for value in values:
#	print(value)