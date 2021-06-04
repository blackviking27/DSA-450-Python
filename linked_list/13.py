# Quick Sort on Linked List
# Sort the given Linked List using quicksort. which takes O(n^2) time in worst case 
# and O(nLogn) in average and best cases, otherwise you may get TLE


def sort(start, end):
    if start == None or start == end or start == end.next:
        return

def quick_sort(head):
    # getting the last element 
    n = head
    while n.next != None:
        n = n.next
    sort(head, n)
