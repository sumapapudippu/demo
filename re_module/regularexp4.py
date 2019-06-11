import re
s = input('enter pattern to check')
#m = re.match(s,'abcdefgh')
#m = re.fullmatch(s,'abcdefgh')


if m != None:
	print("Match is available at the begining of the string")
	#print("start index:{} and end index :{}".format(m.start(),m.end()))
else:
	print("Match is not available at the begining of the string")

#3search
s = input('enter pattern to check')
m = re.search(s,'abcdefgh')	
if m! = None:
	print('Match is not available')
	print('First Occurence with start index:{} and end index{}'.format(m.start(),m.end()))
else:
	print('full string not matched')

#4 findall
s = input('enter pattern to check')
m = re.findall('[0-9]','9c1e4gh')
print (m)	
