# Implement two stacks in an array

#Function to push an integer into the stack1.
def push1(a,x):
    global top1, top2
    if top1 < top2 - 1:
        top1 += 1
        a[top1] = x
    
    
#Function to push an integer into the stack2.
def push2(a,x):
    global top2, top1
    if top1 < top2 - 1:
        top2 -= 1
        a[top2] = x
    
#Function to remove an element from top of the stack1.    
def pop1(a):
    global top1
    if top1 >= 0:
        x = a[top1]
        top1 -= 1
        return x
    else:
        return -1
    
#Function to remove an element from top of the stack2.    
def pop2(a):
    global top2
    if top2 <= 100:
        x = a[top2]
        top2 += 1
        return x
    else:
        return -1