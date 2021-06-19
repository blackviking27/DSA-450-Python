# Rearrange characters
# question link => https://practice.geeksforgeeks.org/problems/rearrange-characters4649/1/

class Solution:
    def rearrangeString(self, string):
            n = len(string)
            
            # calculating the frequency of each character
            freq = {}
            for char in string:
                if char not in freq:
                    freq[char] = 1
                else:
                    freq[char] += 1
            max_freq = -1 # count of max character
            max_char = '' # the max character
            for char in freq:
                if freq[char] > max_freq:
                    max_freq = freq[char]
                    max_char = char
            # if it is possiblt to place all the max_character in the even positions
            if not max_freq <= n - max_freq + 1:
                return "-1"
            
            # creating the result string
            res = ['']*n
            idx = 0 # index of string
            while max_freq != 0: # placing all the max characters at even positions
                res[idx] = max_char
                idx += 2
                max_freq -= 1

            freq[max_char] = 0 # making the max char zero since they are all placed
            
            for char in freq: # for other characeters
                while freq[char] > 0:
                    if idx >= n: # if the idx is out of range implies that all the even positions are filed
                        idx = 1 # initialising to fill the odd positions now
                    res[idx] = char
                    idx += 2
                    freq[char] -= 1
            
            return ''.join(res)

# print(rearrangeString("kkk"))