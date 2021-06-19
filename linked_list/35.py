# First non-repeating character in a stream
# Given an input stream of A of n characters consisting only of lower case alphabets. 
# The task is to find the first non repeating character, each time a character is inserted to the stream. 
# If there is no such character then append '#' to the answer.
class Solution:
    def FirstNonRepeating(self, a):
        vis = [0]*26 # counter array for each letter
        v = [] # to maintain the order
        ans = ""
        for i in range(len(a)):
            if vis[ord(a[i]) - ord('a')]  == 0:
                v.append(a[i])
            vis[ord(a[i]) - ord('a')] += 1

            # appending to the answers
            f = 0
            m = len(v)
            for i in range(m):
                # find the first non repeating element
                if vis[ord(v[i]) - ord('a')] == 1:
                    ans += v[i]
                    f = 1
                    break
            if f == 0:
                ans += "#"
        return ans  