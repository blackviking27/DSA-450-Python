# Coin game winner where every player has three choices

def findWinner(x, y, n):

    dp = [0] * (n + 1)
    
    dp[0] = False # A is unable to pick the coin
    dp[1] = True # A picks the only coin that is available since A always starts the game

    for i in range(2, n + 1): # starting the from 2 coins
        # if dp[i -1] is False then it means that B has played his chance and now it is A's chance
        # i - 1>= 0 determines if we can pick the current coin
        if i - 1 >= 0 and dp[i- 1] == False: 
            dp[i] = True
        elif i -x >= 0 and dp[i- 1] == False:
            dp[i] = True
        elif i - y >= 0 and dp[i - 1] == False:
            dp[i]= True
        else:
            dp[i] = False
    return dp[n]

# Driver code
x = 3; y = 4; n = 5
if (findWinner(x, y, n)):
    print('A')
else:
    print('B')