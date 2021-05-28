# K-th element of two sorted Arrays 
# Given two sorted arrays arr1 and arr2 of size M and N respectively and an element K. 
# The task is to find the element that would be at the k’th position of the final sorted array.

arr = [int(x) for x in input("Enter the array : ")]

def kth(arr, target):
    n = len(arr)
    i,j,k = 0,0,0
    
