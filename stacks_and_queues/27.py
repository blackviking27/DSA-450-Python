# Reverse the first “K” elements of a queue

def modifyQueue(q, k):
    stack = []

    # inserting the first k elements into the stack
    for i in range(k):
        stack.append(q.pop(0))
    
    # pushing the elements back into the queue in reverse order
    while stack:
        q.append(stack.pop())
    
    # inserting len(q) - k elements to the back again
    for i in range(len(q) - k):
        temp = q.pop(0)
        q.append(temp)
    
    return q