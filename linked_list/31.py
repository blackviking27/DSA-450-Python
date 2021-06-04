# Multiply two linked lists 
# Given elements as nodes of the two linked lists. 
# The task is to multiply these two linked lists, say L1 and L2.

def multiply(head1, head2):
    mod = 10**9 + 7
    num1 = ""
    curr1 = head1
    while curr1 != None:
        num1 += str(curr1.data)
        curr1 = curr1.next
    
    num2 = ""
    curr2 = head2
    while curr2 != None:
        num2 += str(curr2.data)
        curr2 = curr2.next
    
    return (int(num1) * int(num2)) % mod