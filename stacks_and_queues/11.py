# 	Evaluation of Postfix expression

class Solution:
    def evaluatePostfix(self, S):
        stack = []
        for char in S:
            if char in ['*', '/', '+', '-']:
                b = stack.pop()
                a = stack.pop()
                if char == '*': stack.append(a * b)
                elif char == '/': stack.append(a // b)
                elif char == '+': stack.append(a + b)
                else: stack.append(a - b)
                # print(stack)
            else:
                stack.append(int(char))
        # print(stack)
        return stack.pop()