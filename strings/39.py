# Function to find Number of customers who could not get a computer


from collections import defaultdict
def runCustomerSimulation(computers, seq):
    seen = defaultdict(int)
    ignored = 0 # number of customers ignored
    occupied = 0 # number of computers available

    for customer in seq:
        # if the customer is coming for the first time then
        # seen[customer] will return 0
        if seen[customer] == 0:
            seen[customer] = 1 # they have arrived 
            if occupied < computers:
                occupied += 1
                seen[customer] = 2 # they have occupied the computer
            else:
                # no computer available
                ignored += 1
        else:
            if seen[customer] == 2: # if they were occupying the computer
                occupied -=1
            seen[customer] = 0

    return ignored

print(runCustomerSimulation(3, "GACCBDDBAGEE"))