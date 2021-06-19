# Maximum and minimum of an array using minimum number of comparisons

arr = [int(x) for x in input("Enter the array : ").split()]

def max_and_min(arr):
    n = len(arr)
    if n % 2 != 0:
        arr_min = arr[0]
        arr_max = arr[0]
    else:
        if arr[0] < arr[1]:
            arr_min = arr[0]
            arr_max = arr[1]
        else:
            arr_min = arr[1]
            arr_max = arr[0]
    
    for i in range(n-1):
        if arr[i] < arr[i + 1]:
            if arr[i] < arr_min:
                arr_min = arr[i]
            if arr[i + 1] > arr_max:
                arr_max = arr[i + 1]
        else:
            if arr[i + 1] < arr_min:
                arr_min = arr[i + 1]
            if arr[i] > arr_max:
                arr_max = arr[i]
    
    return arr_min, arr_max

print(max_and_min(arr))