# Queue based approach or first non-repeating character in a stream.

from collections import deque, defaultdict


class Solution:
    def FirstNonRepeating(self, string):
        # keeping the count of the characters
        count = [0]*26

        # queue to store the order of the characters
        # which occur in the string
        q = deque()

        ans = ""
        for char in string:
            # append the character in the queue
            q.append(char)

            # increase the count of that character
            count[ord(char) - ord('a')] += 1

            # checking if character at the front of the
            # queue is repeating or not
            while q:
                if count[ord(q[0]) - ord('a')] > 1:
                    q.popleft()
                else:
                    break

            if q:
                # now appending the character at the front of queue
                #  to the answer since that character is the first
                # non repeating character in the string from left
                ans += q[0]
            else:
                # if queue if empty then no reapeating elements are present
                ans += "#"

        return ans
