# Maximum profit by buying and selling a share at most twice

def maxProfit(prices):
    n = len(prices)
    profit = [0]*n # stores the max profit at the ith position

    # moving from right to left, we consider the max selling price
    selling_price = prices[n-1]

    for i in range(n-2, -1, -1):
        # if current price is greater than the selling_price then it becomes the new selling price
        if prices[i] > selling_price:
            selling_price = prices[i]
        
        # we store the max of previous profit and current profit
        profit[i] = max(profit[i+1], selling_price - prices[i])
    
    # moving from left to right, now we consider the least cost price
    cost_price = prices[0]
    for i in range(1,n):
        if prices[i] < cost_price:
            cost_price = prices[i]
        # we store the max of previous profit and sum of profit in first transaction plus the current profit
        profit[i] = max(profit[i-1], profit[i] + prices[i] - cost_price)
    
    return prices[n-1]

# valley peak approach
def max_profit_valley_peak(prices):
    n = len(prices)
    profit = 0

    for i in range(1, n):
        if prices[i] - prices[i - 1] > 0:
            profit += prices[i] - prices[i - 1]
    
    return profit