# Sort a Stack using recursion

def sortInsert(s, val):
    # if stack is empty or the current element is greater than the element at top of stack

    # for GFG question we need in descending order thus the condition would be
    # if len(s) == 0 or val < s[-1]
    if len(s) == 0 or val > s[-1]:
        s.append(val)
        return
    else:
        top = s.pop()
        sortInsert(s, val)
        s.append(top)

def sort(s):
    if len(s) != 0:
        curr = s.pop()
        sort(s)
        sortInsert(s, curr)