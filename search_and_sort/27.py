# PRATA - Roti Prata
# IEEE is having its AGM next week and the president wants to serve cheese prata after the meeting. 
# The subcommittee members are asked to go to food connection and get P(P<=1000) pratas packed for the function. 
# The stall has L cooks(L<=50) and each cook has a rank R(1<=R<=8). 
# A cook with a rank R can cook 1 prata in the first R minutes 1 more prata in the next 2R minutes, 
# 1 more prata in 3R minutes and so on(he can only cook a complete prata) 
# (For example if a cook is ranked 2.. he will cook one prata in 2 minutes one more 
# rata in the next 4 mins an one more in the next 6 minutes hence in total 12 minutes 
# he cooks 3 pratas in 13 minutes also he can cook only 3 pratas as he does not have enough 
# time for the 4th prata). The webmaster wants to know the minimum time to get the order done.
# Please write a program to help him out

# question link -> https://www.spoj.com/problems/PRATA/

p = int(input("Enter no. of parathas: "))
n = int(input("Enter no. of chefs: "))
arr = [int(x) for x in input("Enter ranks: ").split()]

def check(arr, n, p, mid):
    time = 0
    paratha = 0
    # going through each chef
    for i in range(1, n):
        time = arr[i]
        j = 2
        # adding the parathas that chef can make in time <= mid (time that we gave)
        # and add that number of parathas to the total parathas
        while time<=mid:
            paratha += 1
            time += arr[i]*j
            j += 1
        if paratha >= p:
            return True
    return False

def min_time(p, arr):
    
    lb = 0
    ub = 10**8 # for the worst case when we need to make 1000 parathas using single chef with rank 8
    ans = 0
    while lb <= ub:
        # chekcking if this time is sufficient
        mid = (lb + ub) // 2
        if check(arr, n, p ,mid):
            ans = mid
            ub = mid - 1
        else:
            lb = mid + 1
    return ans


print(min_time(p, arr))
