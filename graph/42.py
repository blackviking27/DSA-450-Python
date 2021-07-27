# Minimise the cashflow among a given set of friends who have borrowed money from each other

def getMin(amount, n):
    idx = 0
    for i in range(1, n):
        if amount[i] < amount[idx]:
            idx = i
    return idx

def getMax(amount, n):
    idx = 0
    for i in range(1, n):
        if amount[i] > amount[idx]:
            idx = i 
    return idx

def minCashFlowRecur(amount, n):
    # max amount to credit or give to another person
    mxCredit = getMax(amount, n)

    # max amount to debit or taken from another person
    mxDebit = getMin(amount, n)

    # when all the transactions are completed
    if amount[mxCredit] == 0 and amount[mxDebit] == 0:
        return 0
    
    min_amt = min(-amount[mxDebit], amount[mxCredit])
    amount[mxCredit] -= min_amt
    amount[mxDebit] += min_amt

    print(f"Person {mxDebit} payed {min_amt} to Person {mxCredit}")

    minCashFlowRecur(amount, n)

def minCashFlow(graph):
    n = len(graph)
    amount = [0]*n

    # need to update the net amount for each person
    for i in range(n):
        for j in range(n):
            amount[i] += graph[j][i] - graph[i][j]
    
    minCashFlowRecur(amount, n)

# driver code
graph = [ [0, 1000, 2000],
          [0, 0, 5000],
          [0, 0, 0] ]
  
minCashFlow(graph)
  