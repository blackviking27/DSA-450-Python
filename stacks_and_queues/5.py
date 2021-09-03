# Check the expression has valid or Balanced parenthesis or not.

class Solution:
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        stack = []
        for char in x:
            if char in ['[', '{', '(']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                
                top = stack.pop()
                
                if top == '(' and char != ')': return False
                elif top == '{' and char != '}': return False
                elif top == '[' and char != ']': return False
        
        return True if len(stack) == 0 else False