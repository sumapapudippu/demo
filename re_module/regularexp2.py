import re
#finditer
 #start(),end() end+1 index match,group() returns matched string

#finditer how many times that matched patter exist in taget(string,text files)
matcher = re.finditer('python','learning python is very easy')
print (matcher)

#ab ===>any pattern
#abaababa ==>target
#total occurence = 3
#first time :0,Second time:3,third time:5
count = 0
matcher = re.finditer('ab','abaababa')
for match in matcher:
	count+=1
	print('match is available at start index',match.start())
	print('match is available at end index',match.end())
	print('match is available at group',match.group())
print('the number of occurences is',count)




