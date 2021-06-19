# Count and Say

class Solution:
    def countAndSay(self, n):
        if n == 1: return "1"
        if n == 2: return "11"
        s = "11"
        for i in range(3, n + 1):
            s += "$" # adding '$' in order to count the last element too
            temp = "" # stores the new string
            c = 1 # keeps count of the character
            for j in range(1, len(s)):
                if s[j] != s[j - 1]:
                    temp += str(c) # addnig the count of that number 
                    temp += s[j - 1] # adding the number itself
                    c = 1 # initialising the count to 1 for current number
                else:
                    c += 1
            s = temp # s becomes the new string
        
        return s