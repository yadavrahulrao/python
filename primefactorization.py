# to find factors of a number 

import math


def factors(n):
	

	while n % 2 == 0:
		print(2)
		n = n // 2
		

	for i in range(3,int(math.sqrt(n))+1):
		
		while n % i== 0:
			print(i)
			n = n // i
			

	if n > 2:
		print(n)
		

n = int(input("enter number: "))
factors(n)


