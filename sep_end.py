'''doc string'''
print(10, 20, 30, sep='-')
#input: 10 20 30 
#         A B C
#output:10:20:30:A:B:C
print(10, 20, 30, sep=':', end=':')
print('A', 'B', 'C', sep=':')
#input return str
#eval return python obj
variable = eval(input('enter the list of elements'))
print(type(variable))
