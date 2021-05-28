# Arithmetic Number
# Given three integers  'A' denoting the first term of an arithmetic sequence , 
# 'C' denoting the common difference of an arithmetic sequence and an integer 'B'. 
# you need to tell whether 'B' exists in the arithmetic sequence or not
# Question link -> https://practice.geeksforgeeks.org/problems/arithmetic-number2815/1

# a-> initial number, b -> target number, c-> difference
a, b, c = [int(x) for x in input("Enter a, b, c: ").split()]

# genetal formula b = a + (n-1) * c

def if_in_AP(initial, target, diff):
        if diff == 0:
            if initial == target:
                return 1
            else:
                return 0
        if (target - initial) / diff < 0:
            return 0
        else:
            if (target - initial) % diff == 0:
                return 1
            else:
                return 0

print(if_in_AP(a, b, c))