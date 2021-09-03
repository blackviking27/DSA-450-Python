# Leetcode- reorganize strings

from queue import PriorityQueue as pq


class Solution:
    def reorganizeString(self, s: str) -> str:
        # using the max heap

        # getting the frequency of each character
        freq = {}
        for char in s:
            freq[char] = 1 + freq.get(char, 0)

        # putting the elements according to their frequency in max heap
        q = pq()

        for char in freq:
            # putting negative since default implementation of
            # priority queue is min heap, thus when highest value is multiplid by -1 it
            # becomes the smallest value
            q.put([-1 * freq[char], char])

        # initially taking the prev character as # with frequency -1
        prev = [1, '#']

        # to store the answer
        ans = ""
        # print(q.queue)

        while not q.empty():
            count, char = q.get()
            ans += char

            # if prev character has frequency greater than 0
            # we are taking negative since we have multiplied with -1
            # to make min heap as max heap
            if prev[0] < 0:
                q.put(prev)

            # decreasing the freq of current character
            prev = [count + 1, char]
            # print(prev)

        return ans if len(ans) == len(s) else ""
