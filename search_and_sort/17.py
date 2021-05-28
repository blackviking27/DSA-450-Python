# Minimum Swaps to Sort
# Given an array of n distinct elements.
# Find the minimum number of swaps required to sort the array in strictly increasing order.

# Input
# arr = [int(x) for x in input("Enter the array : ").split()]
arr = [1, 5, 4, 3, 2]

# Using the graph method
def min_swap(arr):
	v = []
	n = len(arr)
	for i in range(n):
		v.append([arr[i], i])
	vis = {k: False for k in range(n)}
	ans = 0
	v.sort()
	for i in range(n):
		if vis[i] or v[i][1] == i:
			continue
		
		cycle = 0
		j = i

		while not vis[j]:
			vis[j] = True
			j = v[j][1]
			cycle += 1
		if cycle > 0:
			ans += (cycle - 1)
	return ans

	# Weird solution, I did not understand but somehow works
	# for i in range(n):
	#     if (vec[i][1] == i):
	#         continue
	#     else:
	#         vec[i][0], vec[vec[i][1]][1] = vec[vec[i][1]][1], vec[i][0]
	#         vec[i][1], vec[vec[i][1]][1] = vec[vec[i][1]][1], vec[i][1]

	#     if (vec[i][1] != i):
	#         i -= 1
	#     # print(i)
	#     # print(vec)
	#     print(ans)
	#     ans += 1

	# return ans

print(min_swap(arr))


