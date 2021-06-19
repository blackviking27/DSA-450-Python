# Word Break

# without DP
def wordBreak(string, dictionary):
    i = 0
    # going through each word in dictionary
    while i < len(dictionary):
        l = len(dictionary[i])
        s = string[:l] # taking a  subsrting of size equal to the current word in dictionary
        if s == dictionary[i]: # checking if substring and word are equal
            # if they are euqal then we found a part of the string in dictionary
            # we update the string to other part of string which we still haven't found
            string = string[l:]
            i = 0 # starting from the first word of dictionary again
        else:
            i += 1 # if we didn't find the current word then move to the next word
    
    # if length of string is zero implies that we were able to form the complete string
    if len(string) == 0:
        return 1
    else:
        return 0

