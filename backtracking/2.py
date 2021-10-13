# Word Break - Part 2
# Given a string s and a dictionary of words dict of length n,
# add spaces in s to construct a sentence where each word is a
# valid dictionary word. Each dictionary word can be used more
# than once. Return all such possible sentences.


class Solution:

    def solve(self, idx, path, dict, s):

        # if we have reached the end then we are able to match all the
        # words in the string
        if idx == self.m:
            self.res.append(" ".join(path))
            return

        # matching words from the dict in the string from the current index
        for word in dict:
            n = len(word)
            # if we have enough characters left
            if idx + n <= self.m:
                # if we match the word
                if s[idx:idx + n] == word:
                    path.append(word)
                    # find the reaming string in the dict
                    self.solve(idx + n, path, dict, s)

                    path.pop()  # backtracking

    def wordBreak(self, n, dict, s):
        self.m = len(s)  # length of string
        self.res = []  # to store the result

        self.solve(0, [], dict, s)
        return self.res
