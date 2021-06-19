# Smallest window in a string containing all the characters of another string

class Solution:

    def smallestWindow(self, s, p):
        len1 = len(s)
        len2 = len(p)
        
        # if length of pattern string is greater than string
        if len1 < len2:
            return -1
        
        hash_pat = [0] * 256
        hash_str = [0] * 256

        # counting the occurences of the characters in the string
        for i in range(len2):
            hash_pat[ord(p[i])] += 1
        
        start = 0 # start index of window
        start_index = -1 # stores the starting index of window of min answer
        min_len = float('inf')

        count = 0
        for i in range(len1):
            # count the occurence of character of string
            hash_str[ord(s[i])] += 1

            # checking if we have the characters
            if hash_str[ord(s[i])] <= hash_pat[ord(s[i])]:
                count += 1
            
            if count == len2:
                while hash_str[ord(s[start])] > hash_pat[ord(s[start])] or hash_pat[ord(s[start])] == 0:
                    if hash_str[ord(s[start])] > hash_pat[ord(s[start])]:
                        hash_str[ord(s[start])] -= 1
                    start += 1
                
                len_window = i -start + 1
                if min_len > len_window:
                    min_len = len_window
                    start_index = start
                    
        if start_index == -1:
            return -1
        else:
            return s[start_index: start_index + min_len]