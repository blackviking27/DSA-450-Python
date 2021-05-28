# ANARC05B - The Double HeLiX
#  Two ﬁnite, strictly increasing, integer sequences are given. Any common integer between the two sequences constitute an intersection point. Take for example the following two sequences where intersection points are
# First= 3 5 7 9 20 25 30 40 55 56 57 60 62
# Second= 1 4 7 11 14 25 44 47 55 57 100
# You can ‘walk” over these two sequences in the following way:
# You may start at the beginning of any of the two sequences. Now start moving forward.
# At each intersection point, you have the choice of either continuing with the same sequence you’re currently on, or switching to the other sequence.

# Question link : https://www.spoj.com/problems/ANARC05B/ 

a1 = [int(x) for x in input("Enter 1st arr: ").split()]
a2 = [int(x) for x in input("Enter 2nd arr: ").split()]

def max_sum(a1, a2):
    n = len(a1)
    m = len(a2)
    s1, s2 = 0, 0
    i, j = 0, 0 # pointers to keep track of the position
    ma = 0 # max sum
    # traversing both the arrays and adding sums individually
    while i < n and j < m:
        if a1[i] < a2[j]:
            s1 += a1[i]
            i += 1
        elif a2[j] < a1[i]:
            s2 += a2[j]
            j += 1
        else:
            ma = ma + max(s1, s2) + a1[i]
            i += 1
            j += 1
            s1, s2 = 0, 0
    
    while i < n:
        s1 += a1[i]
        i += 1
    while j < m:
        s2 += a2[j]
        j += 1
    ma += max(s1 , s2)
    return ma

print(max_sum(a1[1::], a2[1::]))
    