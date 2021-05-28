# Given an array Arr of N positive integers. 
# Your task is to find the elements whose value is equal to that of its index value.

arr = [int(x) for x in input("Enter the array : ").split()]

res = []
for i in range(len(arr)):
    if i + 1 == arr[i]:
        res.append(i + 1)
print(res)