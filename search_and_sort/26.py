# Smallest factorial number
# Given a number n. The task is to find the smallest number whose factorial 
# contains at least n trailing zeroes

n = int(input("Enter n: "))

# check if the number of trailing zeros is atleast n
def check(p, n):
	count = 1
	f = 5
	while f <= p:
		count += p // f
		f *= 5
	if count >= n:
		return True
	else:
		return False

def find_min(n):
	if n == 1:
		return 5
	
	low = 0
	high = 5*n

	while low < high:
		mid = (low + high) // 2

		if check(mid, n):
			high = mid
		else:
			low = mid + 1

	return low