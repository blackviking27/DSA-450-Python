# Minimum sum of squares of character counts in a given string after removing “k” characters.

from queue import PriorityQueue


class Solution:
    def minValue(self, s, k):

        # if k is more than len(s) then all the characters will be removed
        if k > len(s):
            return 0

        # create a frequency array
        freq = [0]*26

        # counting the frequency of each character
        for char in s:
            freq[ord(char) - ord('a')] += 1

        # creating the priority queue
        q = PriorityQueue()

        for i in range(26):
            # inserting negative so that the greatest positive becomes the lowest
            # and is pushed to the front
            q.put(-1 * freq[i])

        # now remove the k elements
        for i in range(k):
            temp = q.get()
            # reduce the frequency
            temp += 1
            q.put(temp)

        # getting the sum
        res = 0
        while not q.empty():
            # square of any negative number is positive
            res += q.get() ** 2

        return res
