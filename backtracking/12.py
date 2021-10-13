# Largest number in K swaps

class Solution:

    def solve(self, idx, k, s):
        # if no swaps are left or we have reached the end
        if k == 0 or idx == self.n:
            return

        # finding the max element on the right of current element
        max_el = s[idx]  # assuming that the current element is max element
        for i in range(idx + 1, self.n):
            max_el = max(max_el, s[i])

        # if the current element and max elment are not same then we will use a swap
        if max_el != s[idx]:
            k -= 1

        # now swapping with all the max_element on the right side
        # one by one
        for i in range(self.n - 1, idx - 1, -1):
            if s[i] == max_el:
                # swapping
                s[i], s[idx] = s[idx], s[i]

                # finding the max number
                self.max = max(self.max, int("".join(s)))

                # recursively calling for the next index
                self.solve(idx + 1, k, s)

                # backtracking
                s[i], s[idx] = s[idx], s[i]

    def findMaximumNum(self, s, k):
        self.n = len(s)  # total number of elements
        self.max = float('-inf')

        num = list(s)  # creating a list so that we can swap elements
        self.solve(0, k, num)
        return self.max
