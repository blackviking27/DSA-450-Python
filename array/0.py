# 	Reverse the array

arr = [int(x) for x in input("Enter the array : ").split()]

def arr_rev(arr):
    s = 0
    e = len(arr) - 1
    while s <= e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1
    
    return arr

print(arr_rev(arr))