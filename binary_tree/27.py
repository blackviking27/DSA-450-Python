# Find largest subtree sum in a tree

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def solve(self, root):
        if root is None:
            return 0

        # taking the current sum at the current node
        val = root.data + self.solve(root.left) + self.solve(root.right)
        self.ans = max(val, self.ans)

        return val

    def largest_sum(self,root):
        if root is None:
            return 0
        self.ans = float('-inf') # taking the minimum value
        self.solve(root)
        return self.ans

'''
            1 
          /   \ 
         /      \ 
        -2       3 
        / \     / \ 
        / \     / \ 
       4   5  -6   2 
'''
root = newNode(1) 
root.left = newNode(-2) 
root.right = newNode(3) 
root.left.left = newNode(4) 
root.left.right = newNode(5) 
root.right.left = newNode(-6) 
root.right.right = newNode(2) 

solution = Solution()
print(solution.largest_sum(root))