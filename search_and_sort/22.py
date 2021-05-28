# Allocate minimum number of pages
# You are given N number of books. Every ith book has Ai number of pages. 
# You have to allocate books to M number of students. There can be many ways or permutations to do so. 
# In each permutation, one of the M students will be allocated the maximum number of pages. 
# Out of all these permutations, the task is to find that particular permutation in which the maximum number 
# of pages allocated to a student is minimum of those in all the other permutations and print this minimum value.
# Each book will be allocated to exactly one student. Each student has to be allocated at least one book.

n = int(input("Enter n : "))
arr = [int(input("Enter the array : "))]
m = int(input("Enter the number of students : "))

def solve(arr, n, mid, m):
    std = 1
    sum_pages = 0
    for i in range(n):
        # if any element by itself is greater than the mid element
        if arr[i] > mid:
            return False
        if sum_pages + arr[i] > mid: # if sum of pages till arr[i] is greater than mid
            std += 1
            sum_pages = arr[i]
            if std > m:
                return False
        else:
            sum_pages += arr[i]
    return True

def get_min_max(arr, m):
    total_pages = 0
    for page in arr:
        total_pages += page

    lb = 0
    ub = total_pages
    ans = 0

    while lb <= ub:
        mid = (lb + ub) // 2
        if solve(arr, n, mid, m):
            ans = mid
            ub = mid - 1
        else:
            lb = mid + 1
    return ans

