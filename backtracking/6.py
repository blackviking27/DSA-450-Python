# Given a string, print all possible palindromic partitions
# question link ==> https://leetcode.com/problems/palindrome-partitioning/

class Solution:

    # function to check for palindrome
    def isPalindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def solve(self, idx, path, s):
        # base case
        # if we reach the end of the strig
        if idx == self.n:
            self.res.append(path[:])
            return

        # now trying to find the palindrome substring:
        for i in range(idx, self.n):
            # checking if current substring is a palindrome or not
            if self.isPalindrome(s, idx, i):
                new_str = s[idx:i + 1]  # the new string
                path.append(new_str)
                self.solve(i + 1, path, s)
                path.pop()

    def partition(self, s):
        self.n = len(s)
        self.res = []  # to store the answer
        self.solve(0, [], s)

        return self.res
