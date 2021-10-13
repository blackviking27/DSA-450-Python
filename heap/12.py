# Is Binary Tree Heap

from collections import deque


class Solution:
    def isHeap(self, root):
        q = deque([root])
        end = False  # tells if we have seen a None
        while len(q) != 0:

            curr = q.popleft()  # taking the first element

            if curr.left:  # if left child is present
                if end or curr.left.data >= curr.data:
                    return False
                q.append(curr.left)

            else:
                end = True  # if none then it should be the last node in tree

            if curr.right:
                if end or curr.right.data >= curr.data:
                    return False
                q.append(curr.right)

            else:
                end = True

        return True
