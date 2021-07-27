# Longest Palindromic Substring

class Solution:
    def longestPalin(self, s):
        n = len(s)
        start = 0
        max_len = 1
        
        for i in range(2, n):
            # for even length of substring
            low = i - 1
            high = i
            
            while low >= 0 and high < n and s[low]==s[high]:
                if high - low + 1 > max_len:
                    start = low
                    max_len = high - low + 1
                low -= 1
                high += 1
            
            # for odd length of substring
            low = i - 1
            high = i + 1
            while low >= 0 and high < n and s[low] == s[high]:
                if high - low  + 1 > max_len:
                    start = low
                    max_len = high - low + 1
                low -= 1
                high += 1
        return s[start: start + max_len]
