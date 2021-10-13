# Permutations of a given string

class Solution:

    def solve(self, idx, s):
        # base case
        # we have reached the end of the array
        if idx == self.n:
            self.res.append("".join(s))
            return

        # swapping with other element and calling for permutations
        for i in range(idx, self.n):
            s[idx], s[i] = s[i], s[idx]
            self.solve(idx + 1, s)
            s[idx], s[i] = s[idx], s[i]  # backtracking

    def find_permutations(self, S):
        s = list(S)  # converting to list so that we can perform swapping
        self.res = []  # to store answer
        self.n = len(s)

        self.solve(0, s)
