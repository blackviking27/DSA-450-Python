# Find the next Greater element

class Solution:
    def nextLargerElement(self,arr,n):
        # stores the index of the element
        stack = []
        ans = [-1]*n

        # storing the index of first element in the stack
        stack.append(0)

        for i in range(1, n):
            # taking the current element 
            curr = arr[i]
            
            # taking the element at top
            top = stack.pop()

            while arr[top] < curr:
                ans[top] = curr
                if len(stack) == 0:
                    break
                top = stack.pop()

            # if the element at the top is greater than the curr element
            if arr[top] > curr:
                stack.append(top)

            # appending the current element index
            stack.append(i)
        
        return ans