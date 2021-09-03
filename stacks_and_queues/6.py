# Reverse a string using Stack

def reverse(S):
    stack = []
    for char in S:
        stack.append(char)
    
    string = ""
    while stack:
        string += stack.pop()
    
    return string