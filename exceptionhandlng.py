print("Hai")
#print(10/0)
try:
	print(10/0)
#xcept ZeroDivisionError as msg:
except (ZeroDivisionError,ValueError) as msg:
	print("exception raised :",msg)
#exception raised not raised handled or not handled
finally:
	print("Hello")
        
#2 example
try:
	print('try')
	print(10/0)
except:
	print('except')
finally:
	print('finally')

#3rd Example
try:qa
	print('try')
	print(10/0)
except 	ValueError:
	print('except')
else:
	print('else')

finally:
	print('finally')

#User defined Exceptions
