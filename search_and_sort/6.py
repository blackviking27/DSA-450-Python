#Given an unsorted array of size n. Array elements are in the range from 1 to n. 
# One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers.

arr = [int(x) for x in input("Enter the array : ").split()]

repeat, miss = 0, 0

for i in range(len(arr)):
    if arr[abs(arr[i]) - 1] < 0:
        repeat = abs(arr[i])
    else:
        arr[abs(arr[i]) - 1] *= -1
    
for i in range(len(arr)):
    if arr[i] > 0:
        miss = i + 1

print(repeat, miss)
