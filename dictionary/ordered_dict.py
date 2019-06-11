from collections import OrderedDict
d={'banana':3,'apple':4,'pear':1,'orange':2}
#print(sorted(d.items(),key=lambda t:t[0]))
print(OrderedDict(sorted(d.items(),key=lambda t:t[0])))
#print(sorted(d.items(),key=lambda t:t[1]))
print(OrderedDict(sorted(d.items(),key=lambda t:t[1])))
print(OrderedDict(sorted(d.items(),key=lambda t:len(t[0]))))