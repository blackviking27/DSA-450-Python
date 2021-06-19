# Rearrange array in alternating positive & negative items with O(1) extra space

n = int(input("Enter the length of array : "))
arr = list(map(int, input('Enter the array : ').split()))

def arrange(arr, n):
    i = 0 # pointing at the start
    j = n - 1 # poiting at the end

    while i <= j:
        if arr[i] < 0 and arr[j] > 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] > 0 and arr[j] < 0:
            i += 1
            j -= 1
        elif arr[i] > 0:
            i += 1
        elif arr[j] < 0:
            j -= 1
    print(*arr)
    if i == 0 or i == n: # Either they are all negative or all positve
        print(*arr)
    else:
        k = 0
        while k < n and  i < n:
            arr[k], arr[i] = arr[i], arr[k]
            k += 2
            i += 1
        print(*arr)

arrange(arr, n)
