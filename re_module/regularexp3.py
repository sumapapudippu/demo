import re
#[abc] --> either a or b or c
#[^abc] --> except a or b or c
#[a-z] -->any lowe case alphabet symbols
#[A-Z]
#[a-zA-z0-9]
#\s --> space char
#\S --> Except space char ,\d,\D,\w,\W, . --> any char
matcher = re.finditer('[^abc]','a7b@k9z')
for m in matcher:
	print(m.start(),'......',m.group())

matcher = re.finditer('[a-z]','a7b@k9z')
for m in matcher:
	print(m.start(),'......',m.group())	

matcher = re.finditer('[0-9]','a7b@k9z')
for m in matcher:
	print(m.start(),'......',m.group())	

matcher = re.finditer('[a-zA-Z0-9]','a7b@k9z')
for m in matcher:
	print(m.start(),'......',m.group())	

print()
matcher = re.finditer('.','a7b@k9z')
for m in matcher:
	
	print(m.start(),'......',m.group())	

#quantifiers
# + --> atleast one char
# * --->any num of char,including zero num also
# ? --> either one 'a'or zero num of 'a'
# a{3} -->exactly 3 char
# a{2,5} --> min 2 and max 5
'''
0 ...... aa
2 ......
3 ......
4 ...... aaa
7 ......
8 ...... a
9 ......
'''
print()
matcher = re.finditer('a*','aabbaaaba')
for m in matcher:
	
	print(m.start(),'......',m.group())	

print()
matcher = re.finditer('a?','aabbaaaba')
for m in matcher:
	
	print(m.start(),'......',m.group())	

print()
matcher = re.finditer('a{3}','aabbaaaba')
for m in matcher:
	
	print(m.start(),'......',m.group())	
