# Populate Inorder Successor for all nodes

class Solution:
    def populate(self, root):
        if root is None: return
        
        self.populate(root.left)
        
        if self.prev != None:
            self.prev.next = root

        self.prev = root
        self.populate(root.right)

    def populateNext(self, root):
        self.prev = None
        self.populate(root)
        return root