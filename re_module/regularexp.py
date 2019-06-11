import re
#comiple
#finditer
 #start(),end() end+1 index match,group() returns matched string
#create pattern(Regular exp) object
pattern = re.compile('python')
print(type(pattern))
#finditer how many times that matched patter exist in taget(string,text files)
matcher = pattern.finditer('learning python is very easy')
print (matcher)

#ab ===>any pattern
#abaababa ==>target
#total occurence = 3
#first time :0,Second time:3,third time:5
count = 0
pattern = re.compile('ab')
matcher = pattern.finditer('abaababa')
for match in matcher:
	count+=1
	print('match is available at start index',match.start())
	print('match is available at end index',match.end())
	print('match is available at group',match.group())
print('the number of occurences is',count)




