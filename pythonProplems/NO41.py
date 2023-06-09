import math

n=12 #Replace with the desired valueof n 
sum =0

for i in range(1, n+1):
	factorial = 1
	for j in range(1, i+1):
		factorial*=j
	sum+=factorial

print("The sum of the series is: ", sum)