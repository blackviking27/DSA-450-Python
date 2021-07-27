# Top View of Binary Tree 

from collections import deque
class Solution:
    def topView(self,root):
        if root is None: return []

        distance = {} # map which checks if a horizontal distance is already covered or not
        q = deque([[root, 0]]) # we take node and its horizontal distance
        mi = float('inf') # the max distance from root node to the left
        while len(q) != 0:
            curr = q.popleft()
            if curr[1] not in distance: # if horizontal distance is not mapped yet
                distance[curr[1]] = curr[0].data 
                mi = min(mi, curr[1]) # taking the extreme distance of left
            if curr[0].left != None: q.append([curr[0].left, curr[1] - 1]) # adding left node of current node
            if curr[0].right != None: q.append([curr[0].right, curr[1] + 1]) # adding right node of current node
        ans = []
        # traversing the map from minimum distance till max distance and appending the answer 
        while mi in distance:
            ans.append(distance[mi])
            mi += 1
        return ans