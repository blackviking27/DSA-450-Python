# Split the binary string into substrings with equal number of 0s and 1s

def maxSubstr(string):
    count0 = 0 # counts the number of '0's till that index 
    count1 = 0 # counts the number of '1's till that index
    count = 0 # counts the number of substrings which have the same number 0s and 1s

    for i in range(len(string)):
        if string[i] == '0':
            count0 += 1
        else:
            count1 += 1
        
        # checking if number of 1s and 0s are equal till here
        if count1 == count0:
            count += 1
    
    return count if count > 0 else 0

string = input("Enter the binary string: ")
print(maxSubstr(string))