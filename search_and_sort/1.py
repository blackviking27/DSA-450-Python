#Given a sorted array arr containing n elements with possibly duplicate elements, 
# the task is to find indexes of first and last occurrences of an element x in the given array.

# Solution

arr = [int(x) for x in input("Enter the array : ").split()]
m = int(input("Enter the number to find : "))

# using binary tree

# first occurence
def first_index(arr, m):
    res = 0
    left = 0
    right = len(arr) - 1
    while right >= left:
        mid = (left + right)//2
        if arr[mid] < m:
            left = mid + 1
        elif arr[mid] > m:
            right = mid - 1
        else:
            res = mid
            right = mid - 1
    return res
    
# last occurence
def last_index(arr, m):
    res = 0
    left = 0
    right = len(arr) - 1
    while right >= left:
        mid = (left + right) // 2
        if arr[mid] < m:
            left = mid + 1
        elif arr[mid] > m:
            right = mid - 1
        else:
            res = mid
            left = mid + 1
    return res

print(first_index(arr, m))
print(last_index(arr, m))