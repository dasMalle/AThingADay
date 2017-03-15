#project euler problem 2
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def evenFib2():
	a, b = 1, 1
	total = 0
	while a <= 4000000:
		if a % 2 == 0:
			total += a	
		tmp = a
		a = b
		b = tmp + b 
		#a, b = b, a+b 
	print (total)

evenFib2()
