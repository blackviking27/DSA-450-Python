# Stickler Thief
# Stickler the thief wants to loot money from a society having n houses in a single line. 
# He is a weird person and follows a certain rule when looting the houses. According to the rule,
# he will never loot two consecutive houses. At the same time, he wants to maximize the amount he loots. 
# The thief knows which house has what amount of money but is unable to come up with an optimal looting strategy.
# He asks for your help to find the maximum money he can get if he strictly follows the rule. 
# Each house has a[i] amount of money present in it.

n = int(input("Enter length : "))
arr = [int(x) for x in input("Enter the array : ").split()]

# Time complexity O(n) and space complexity O(n)
def give_max(arr, n):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    
    dp = [0]*n # Creating an array which has n zeros
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        # dp[i] represents the max money stolen till that house number
        dp[i] = max(arr[i] + dp[i-2], dp[i -1])
    return dp[-1]

print(give_max(arr, n))