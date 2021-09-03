# Maximum Rectangular Area in a Histogram

class Solution:
    # Getting TLE for below solution on GFG platform
    def getMaxArea(self,histogram):
        n = len(histogram)
        left = [0]*n
        right = [0]*n
        stack = []
        # filling the left array
        for i in range(n):
            if len(stack) == 0:
                left[i] = 0
                stack.append(i)
            else:
                while len(stack) != 0 and histogram[stack[-1]] >= histogram[i]:
                    stack.pop()
                
                left = stack[-1] + 1 if len(stack) != 0 else 0
                stack.append(i)

        while len(stack) != 0:
            stack.pop()
        
        # filling the right array
        for i in range(n - 1, -1, -1):
            if len(stack) == 0:
                right[i] = n - 1
                stack.append(i) 
            else:
                while len(stack) != 0 and histogram[stack[-1]] >= histogram[i]:
                    stack.pop()
                right[i] = stack[-1] - 1 if len(stack) != 0 else n - 1
                stack.append(i)

        # calculating max area
        max_area = float('-inf')
        for i in range(n):
            max_area = max(max_area, histogram[i]*(right[i] - left[i] + 1))
        
        return max_area
    
    # Accepted solution on GFG
    def maxArea(self, arr):
        stack = []
        idx = 0
        max_area = 0

        while idx < len(arr):
            if not stack or arr[stack[-1]] <= arr[idx]:
                stack.append(idx)
                idx += 1
            else:
                top = stack.pop()
                area = arr[top] * ((idx - stack[-1] - 1) if stack else idx)
                max_area = max(max_area, area)
        
        while stack:
            top = stack.pop()
            area = arr[top] * ((idx - stack[-1] - 1) if stack else idx)
            max_area = max(max_area, area)
        
        return max_area
