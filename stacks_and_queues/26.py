# Reverse a Queue using recursion

from queue import Queue
def reverse(q):
    i = 0
    j = len(q.queue) - 1
    while i <= j:
        q.queue[i], q.queue[j] = q.queue[j], q.queue[i]
        i += 1
        j -= 1
    
    return q