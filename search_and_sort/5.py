# Maximum and minimum of an array using minimum number of comparisons

# comparing in pairs
arr = [int(x) for x in input("Enter the array : ").split()]

min, max, i = 0, 0, 0

# checking if there are odd number of elements in the array
if len(arr) % 2 == 0:
    if arr[0] >= arr[1]:
        max = arr[0]
        min = arr[1]
    else:
        max = arr[1]
        min = arr[0]
    i = 2
else:
    max = arr[0]
    min = arr[0]
    i = 1

while(i < len(arr)):
    if arr[i] > arr[i + 1]:
        if arr[i] > max:
            max = arr[i]
        if arr[i + 1] < min:
            min = arr[i + 1]
    else:
        if arr[i] < min:
            min = arr[i]
        if arr[i + 1] > max:
            max = arr[i + 1]
    i += 2
 
print(max, min)
