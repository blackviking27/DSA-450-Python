# Convert a sentence into its equivalent mobile numeric keypad sequence

def convert_to_key(string):
    
    # stores the number of taps to convert to string
    key = ["2", "22", "222",
       "3", "33", "333",
       "4", "44", "444",
       "5", "55", "555",
       "6", "66", "666",
       "7", "77", "777", "7777",
       "8", "88", "888",
       "9", "99", "999", "9999" ]
    
    res = ''
    for i in range(len(string)):
        char = string[i]
        taps = key[ord(char) - ord('A')] # gives the number of taps on the keypad to get the character
        res += str(taps)

    return res

print(convert_to_key('BAC'))