# Bishu and Soldiers, HackerEarth
# Bishu went to fight for Coding Club. There were N soldiers with various powers. 
# There will be Q rounds to fight and in each round Bishu's power will be varied. 
# With power M, Bishu can kill all the soldiers whose power is less than or equal to M(<=M). 
# After each round, All the soldiers who are dead in previous round will reborn.
# Such that in each round there will be N soldiers to fight. As Bishu is weak in mathematics, 
# help him to count the number of soldiers that he can kill in each round and total sum of their powers

# input 
# arr = [int(x) for x in input("Enter the power of soldiers : ").split()]
# q = int(input("Enter number of rounds : "))


def bishu(arr):
    # Gives the upper bound for the element
    def binary_search(arr, x):
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] <= x:
                l = mid + 1
            else:
                r = mid
        return l

    n = len(arr)
    arr.sort()
    prev_sum = [0]
    sum = 0
    for i in range(n):
        sum += arr[i]
        prev_sum.append(sum)
    print(prev_sum)
    q = int(input("Enter the number of rounds : "))
    for i in range(q):
        power = int(input("Enter bishu's power : "))
        index = binary_search(arr, power)
        print(prev_sum[index])


bishu([1,2,3,4,5,6,7])


# Solution posted on hackerearth forum https://paste.ubuntu.com/p/Q6TqPnCQfN/