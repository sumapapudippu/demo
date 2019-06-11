dict={}
dict[1]='one'
dict[2]='two'
print(dict)
dict['three'] =3
#print (dict[3]) #throws key error
print(dict.get(3,'Not Found'))
dict[3] = 'three' #add new key
dict[1] = 'new one'#update key
dict.update({2:'new two',3:'new three'})
#del dict
del dict['three']
num = dict.pop(1)
print(num)
print (len(dict))

print(list(dict.values()))
print(dict.items()) #dict type
print(list(dict.items())) #list  of tuples having key,value pair
del dict
dict = {'name':'suma','address':'ap','age':27}
for value in dict.values():
	print(value)
for key,value in dict.items():
	print(key,value)
print(list(dict.keys()))		
print(sorted(dict.keys()))
print('name' in dict)

