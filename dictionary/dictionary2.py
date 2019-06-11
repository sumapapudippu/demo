d={}
#inserting or updating
d=dict(a=65,b=66,c=67)
d['d']=68
#or
d.update({'e':69})
#or
d.update(dict(f=70))
#or
d.update(g=71)
print(d)
 #Merging two dictionaries
d2 =dict(h=72,i=73,j=74) 
print(d.update(d2))
print(d)
#d.clear()
#d.pop(j)
#del d['d']
d.__setitem__('k',75) #shouldn't use because of poor performance
print(d)

