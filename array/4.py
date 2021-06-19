# Move all negative numbers to beginning and positive to end with constant extra space

arr = [int(x) for x in input("Enter the array : ").split()]

def move(arr):
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        # if l <, r < 0 move l=l+1 to find the adjacent positive to be replaced
        if left < 0 and right < 0:
            left += 1
        # if l > 0 and r < 0, then simply swipe and move the pointers
        elif left > 0 and right < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        # if both are positive, then move right to find the negative
        elif right > 0 and left > 0:
            right -= 1
        # if l  < 0 and r > 0, move to find a pair satisfying above condition
        else:
            left += 1
            right -= 1

print(move(arr))