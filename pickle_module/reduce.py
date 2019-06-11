#import functools module for reduce()
from functools import reduce

#initializing the list
li = [1,3,5,6,8]
#using reduce to compute sum of list
print("the sum of the list elements is ",end=" ")
print (reduce(lambda x,y:x+y,li))