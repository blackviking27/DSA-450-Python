# Find four elements that sum to a given value

# l, k = [int(x) for x in input("Enter n,k : ").split()]
# arr = [int(x) for x in input("Enter the array : ").split()]
l , k = 7, 23
arr = [10,2,3,4,5,7,8]

def get_quad(arr, k):
    n = len(arr)
    if n < 4:
        return []
    res = []
    arr.sort()
    for i in range(n - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            left = j + 1
            right = n - 1
            sum_i_j = arr[i] + arr[j]
            remain = k - sum_i_j
            while left < right:

                if arr[left] + arr[right] == remain:
                    res.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    # moving left till no same element is present
                    while left < right and arr[left] == arr[left - 1]:
                        left +=1
                    while left < right and arr[right] == arr[right + 1]:
                        right +=1
                elif arr[left] + arr[right] < remain:
                    left += 1
                else:
                    right -= 1
    return res

print(get_quad(arr, k))