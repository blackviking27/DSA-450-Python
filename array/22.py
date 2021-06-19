# Maximum Product Subarray
# Given an array Arr that contains N integers (may be positive, negative or zero). 
# Find the product of the maximum product subarra

class Solution:
	def max_sum_subarr(self, arr, n):
		ma = arr[0] # taking the max till that index
		mi = arr[0] # taking the min till that index
		prod = arr[0] # the max product
		for i in range(1, n):
			if arr[i] < 0:
				# 1. if max > 0 and min > 0, when multiplied with -ve num they will swtich
				# since min has lower negative value than max
				# 2. if max > 0 and min < 0, when multipled with -ve max < 0 and min > 0
				# 3. if max < 0 and min < 0, when multiplied with -ve max will have lower value than min
				# thus, we need to swap min and max every time we encounter negative number
				ma, mi = mi, ma #swapping the two values
			ma = max(ma * arr[i], arr[i])
			mi = min(mi * arr[i], arr[i])
			if ma > prod:
				prod = ma
		return prod