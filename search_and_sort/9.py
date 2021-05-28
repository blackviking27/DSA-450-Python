# Find Pair Given Difference
# Given an array Arr[] of size L and a number N, 
# you need to write a program to find if there exists a pair of elements in the array whose difference is N.


# Input
# l,n = [int(x) for x in input("Enter l, n : ").split()]
# arr = [int(x) for x in input("Enter array : ").split()]

l, n = 78, 6
arr = [5, 20, 3, 2, 5, 80]

arr.sort()
print(arr)
def find_pair(arr):
    n = len(arr)
    i, j = 0, 1
    while i < n and j < n:
        if i != j and arr[j] - arr[i] == l:
            return True
        elif arr[j] - arr[i] < l:
            j += 1
        else:
            i += 1
    return False
    
print(find_pair(arr))




# sorting the array
# arr.sort()

# def binary_search(arr, l, r, x):
#     while r <= l:
#         mid = (l + r) // 2
#         if arr[mid] == x:
#             return 1
#         elif arr[mid] < x:
#             l = mid + 1
#         else:
#             r = mid - 1
#     return -1

# ans = False
# for i in range(len(arr)):
#     add = l + arr[i]
#     res = binary_search(arr, i, len(arr), add)
#     if res:
#         ans = True
#         break
# if ans:
#     print(1)
# else:
#     print(-1)