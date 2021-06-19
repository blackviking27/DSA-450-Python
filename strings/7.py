# Longest Palindrome in a String 

class Solution:
    def longestPalin(self, s):
        start = 0 # start index of the longest palindrome
        end = 1 # length of the string

        for i in range(1, len(s)):
            # finding longest even length palindrome
            low = i - 1
            high = i
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if high - low + 1 > end:
                    start = low
                    end = high - low + 1
                low -= 1
                high += 1
            
            # for odd length of palindrome
            low = i - 1
            high = i + 1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if high - low + 1 > end:
                    start = low
                    end = high - low + 1
                low -= 1
                high += 1
            