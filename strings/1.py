# Palindrome String
# Given a string S, check if it is palindrome or not

class Solution:
    def isPalindrome(self, string):
        i = 0
        j = len(string) - 1
        # travesing from the start and end,
        # comapring values as we move on
        while i <= j:
            if string[i] != string[j]:
                return 0
            i += 1
            j -= 1
        return 1