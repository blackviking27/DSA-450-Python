# Merge K sorted linked lists
# Given K sorted linked lists of different sizes. 
# The task is to merge them in such a way that after merging they will be a single sorted linked list. 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    
    # used to merge the two linked lists
    def merge(self, head1, head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1

        res = None
        if head1.data < head2.data:
            res = head1
            res.next = self.merge(head1.next, head2)
        else:
            res = head2
            res.next = self.merge(head1, head2.next)
        
        return res

    def mergeKLists(self, arr, K):
        last = K - 1
        while last != 0:
            i = 0
            j = last
            while i < j:
                arr[i] = self.merge(arr[i], arr[j])
                i += 1
                j -= 1
                if i >= j:
                    last = j
        
        return arr[0]


class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail=self.tail.next
    
def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk=walk.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        line=[int(x) for x in input().strip().split()]
        
        heads=[]
        index=0
        
        for i in range(n):
            size=line[index]
            index+=1
            
            newList = LinkedList()
            
            for _ in range(size):
                newList.add(line[index])
                index+=1
            
            heads.append(newList.head)
        
        merged_list = Solution().mergeKLists(heads,n)
        printList(merged_list)

# } Driver Code Ends