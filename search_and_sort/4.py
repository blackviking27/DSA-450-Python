# Consider a sample space S consisting of all perfect squares starting from 1, 4, 9 and so on. 
# You are given a number N, you have to output the number of integers less than N in the sample space S.

n = int(input("Enter the number : "))

from math import sqrt

num = int(sqrt(n))
if num * num == n:
    print(num - 1)
else:
    print(num)
