# Given an array A of N elements. Find the majority element in the array.
# A majority element in an array A of size N is an element that appears more than N/2 times in the array.

arr = [int(x) for x in input("Enter the array : ").split()]
n = len(arr)

me = arr[0] # majority element
count = 1
for i in range(1, n):
    if arr[i] == me:
        count += 1
    else:
        count -= 1
    
    if count == 0:
        me = arr[i]
        count = 1

c = 0 # checking if the possible majority element is actually majority element
for el in arr:
    if el == me:
        c += 1
if c > n // 2:
    print("Majority Element : " + str(me))
else:
    print("Majority Element does not exist")