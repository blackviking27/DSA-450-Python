# Construct Binary Tree from String with bracket representation

# node class
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


# O(n2) solution
class Solution_1:

    # function to find the closing bracket for the opening bracket
    def findIdx(self, string, start, end):
        if start > end:
            return -1

        stack = []
        for i in range(start, end + 1):
            # if opening bracket then push it onto the stack
            if string[i] == '(':
                stack.append(string[i])
            elif string[i] == ")":
                stack.pop()  # removing the top element

                # if stack is empty then the current closing parenthesis
                # is the required parenthesis
                if len(stack) == 0:
                    del stack
                    return i

        del stack
        return -1

    def buildTreeFromString(self, string, start, end):
        # start crosses end then just return
        if start > end:
            return

        # creating the node
        curr = Node(ord(string[start]) - ord('0'))
        index = -1  # tells us if we have left child or not

        if start + 1 <= end and string[start + 1] == '(':
            index = self.findIdx(string, start + 1, end)

        # if left subtree exists
        if index != -1:
            # creating the left subtree by ignoring the outer opening and closing
            # brackets in string string
            curr.left = self.buildTreeFromString(string, start + 2, index - 1)
            curr.right = self.buildTreeFromString(string, index + 2, end - 1)

        return curr

    def preorder(self, root):
        if root is None:
            return

        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)


# O(n) solution
class Solution_2:
    pass


s = Solution_1()
string = "4(2(3)(1))(6(5))"

root = s.buildTreeFromString(string, 0, len(string) - 1)

s.preorder(root)
