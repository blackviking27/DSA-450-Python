# Minimum Swaps for Bracket Balancing

class Solution:
    def minimumNumberOfSwaps(self,s):
        pos = [] # stores the position of '['
        for i in range(len(s)):
            if s[i] == '[':
                pos.append(i)
        
        idx = 0 # points to the next index of '['
        ans = 0
        count = 0 # keeps the count of '[' and ']'
        s = list(s) # converting the string to list inorder to swap the characters
        for i in range(len(s)):
            if s[i] == '[':
                count += 1
                idx += 1
            else:
                count -= 1
                if count < 0:
                    ans += pos[idx] - i
                    s[i], s[pos[idx]] = s[pos[idx]], s[i]
                    count = 1
                    idx += 1
        return ans

    # without using O(n) extra space, above solution works as well
    def min_swaps(self, s):
        open_br = 0
        close_br = 0
        fault = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == ']':
                close_br += 1
                fault = close_br - open_br # since the number of close are greater than open
            else:
                open_br += 1
                if fault > 0: # if any unbalanced ']' exist
                    ans += fault
                    fault -= 1 # since the single '[' will balance one ']'
        return ans
