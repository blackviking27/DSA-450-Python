# Smallest distinct window 

class Solution:
    def findSubString(self, string):
        char_map = {}
        # creating the map of unique characters
        for char in string:
            if char not in char_map:
                char_map[char] = 0
        
        n = len(char_map) # total number of distince characters
        i = 0
        char_map[string[0]] = 1 # since the first character is already being count in the window
        j = 1
        count = 1 # keeps the count of distinct characters in a window
        ans = float('inf')
        while j < len(string) and i <= j:
            if count < n:
                if char_map[string[j]] == 0: count += 1
                char_map[string[j]] += 1
                j += 1
            elif count == n:
                ans = min(ans, j - i)
                if char_map[string[i]] == 1: count -= 1 # when a single character is present in the window
                char_map[string[i]] -= 1
                i += 1
        # if j is at end i is at some position then it is possible to find another small string between i and j
        while count == n:
            ans = min(ans, j - i)
            if char_map[string[i]] == 1: count -= 1
            char_map[string[i]] -= 1
            i += 1
        return ans
