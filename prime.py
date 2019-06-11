#taking input from user
number = int(input('enter any number'))
#prime number always greater than one
if number>1:
	for(i in range(2,number//2)):
		#condition true given num is not prime,else number is a prime
		if number%i == 0:
			print("number{} is not prime".format(number))
			break
	else:
		print("{}is a prime number".format(number))
else:
	print("{}is not prime".format(number))


			
