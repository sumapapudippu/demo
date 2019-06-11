'''Doc string'''
#import functools module for reduce()
from functools import reduce
from itertools import accumulate
import operator
#initializing the list
li = [1, 3, 5, 6, 8]
#using reduce to compute sum of list
print("the sum of the list elements is ", end=" ")
#print (reduce((lambda x,y:x+y),li)))
print(reduce((lambda x, y: x-y), li))
#using reduce to compute maximum element from list
print("the max element of the list", end=" ")
print(reduce((lambda x, y: x if x > y else y), li))
#using reduce to compute sum of list
print("the sum of the list elements is ", end=" ")
#print (reduce((lambda x,y:x+y),li)))
print(reduce((operator.add), li))

#printing summation of list using accumulate()
print(list(accumulate(li, (lambda x, y: x+y))))
