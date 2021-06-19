# Roman Number to Integer

def romanToDecimal(string):
    # code here
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = values[string[0]]
    prev = values[string[0]]
    for i in range(1, len(string)):
        if values[string[i]] > prev:
            num += values[string[i]] - (2*prev) # reducing the prev value 2 times since it was already added to the product
        else:
            num += values[string[i]]
        prev = values[string[i]]
    return num