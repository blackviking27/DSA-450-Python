# Parenthesis Checker

class Solution:
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        stack = []
        
        # adding the opening brackets to stack
        for char in x:
            if char in ['(', '{', '[']:
                stack.append(char)
        
            else:
                # if stack is already empty then no opening bracket for current closing bracket
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if curr == '(' and char != ')': return False
                if curr == '{' and char != '}': return False
                if curr == '[' and char != ']': return False
        
        # if stack is empty then all the brakcets are paired
        return True if len(stack) == 0 else False