# EKO - Eko
# Lumberjack Mirko needs to chop down M metres of wood. It is an easy job for him since he has a nifty new woodcutting machine that can take down forests like wildfire. However, Mirko is only allowed to cut a single row of trees.
# Mirko‟s machine works as follows: Mirko sets a height parameter H (in metres), a
# nd the machine raises a giant sawblade to that height and cuts off all tree parts 
# higher than H (of course, trees not higher than H meters remain intact). 
# Mirko then takes the parts that were cut off. For example, if the tree row contains 
# trees with heights of 20, 15, 10, and 17 metres, and Mirko raises his sawblade to 15 
# metres, the remaining tree heights after cutting will be 15, 15, 10, and 15 metres, 
# respectively, while Mirko will take 5 metres off the first tree and 2 metres off the 
# fourth tree (7 metres of wood in total).
# Mirko is ecologically minded, so he doesn‟t want to cut off more wood than necessary. 
# That‟s why he wants to set his sawblade as high as possible. 
# Help Mirko find the maximum integer height of the sawblade that still allows 
# him to cut off at least M metres of wood

n, m = [int(x) for x in input("Enter n, m : ").split()]
arr = [int(x) for x in input("Enter tree heights : ").split()]

def get_height(arr, n, m):
    arr.sort()

    # taking the extreme heights of the trees
    lb = arr[0]
    ub = arr[-1]
    ans = 0

    while lb <= ub:
        mid = (lb + ub) // 2

        # calculating the height cut if height of sawblade is eaqual to mid
        total_cut = 0
        for h in range(n):
            if arr[h] > mid:
                total_cut += arr[h] - mid
        
        # checking if we are getting the atleast the min required height
        if total_cut >= m:
            ans = mid
            lb = mid + 1
        else:
            ub = mid - 1
    return ans

print(get_height(arr, n, m))