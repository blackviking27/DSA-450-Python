# Quick Sort on Linked List
# Sort the given Linked List using quicksort. which takes O(n^2) time in worst case
# and O(nLogn) in average and best cases, otherwise you may get TLE

def partition(start, end):
    if start == end or start == None or end == None:
        return start

    pivot_prev = start
    curr = start
    pivot = end.data

    while start != end:
        if start.data < pivot:
            pivot_prev = curr
            curr.data, start.data = start.data, curr.data
            curr = curr.next
        start = start.next

    curr.data, end.data = end.data, curr.data
    return pivot_prev


def sort(start, end):
    if start == None or start == end or start == end.next:
        return

    pivot_prev = partition(start, end)
    sort(start, pivot_prev)

    if pivot_prev != None and pivot_prev == start:
        sort(pivot_prev.next, end)
    elif pivot_prev != None and pivot_prev.next == next != None:
        sort(pivot_prev.next.next, end)


def quick_sort(head):
    # getting the last element
    start = head
    end = head
    while end.next != None:
        end = end.next
    sort(start, end)
