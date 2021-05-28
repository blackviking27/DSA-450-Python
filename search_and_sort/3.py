# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is rotated at an unknown pivot index k 
# (0 <= k < nums.length) such that the resulting array is 
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the rotation and an integer target, return the index of target if it is in nums,
# or -1 if it is not in nums.

arr = [int(x) for x in input("Enter the rotated sorted array : ").split()]
target = int(input("Enter the number to find in array : "))

def find(arr, x):
    left = 0
    right = len(arr) - 1
    while (right >= left):
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        # checking of the left side is sorted or not
        elif arr[mid] >= arr[left]:
            # checking if the target is in the sorted sub arary or not
            if x >= arr[left] and x <= arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # checking if the target lies in the right side or not
            if x >= arr[mid] and x <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    # when the number is not present in the array
    return -1

print(find(arr, target))