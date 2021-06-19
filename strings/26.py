# Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs):
        sl = float('inf') # taking the max possible length
        prefix = ""
        # finding the smallest string in the 'strs' array
        for string in strs:
            if len(string) < sl:
                sl = len(string)
                prefix = string[:len(string)]

        # now checking if the smallest word is prefix for every word in the 'strs' array
        i = 0
        while i < len(strs):
            if prefix == "": # if prefix is empty then break the loop
                break
            if prefix != strs[i][:len(prefix)]: # comparing the same length of characters
                prefix = prefix[:len(prefix) - 1] # if not found then reduce the size of prefix and search again
                i = 0
            else:
                i += 1 # move to the next word in 'strs' string
        return prefix