# Longest Prefix Suffix

class Solution:
	def lps(self, s):
		n = len(s)

		# used to store the longesr prefix and suffix
		lps = [0] * n

		l = 0 # length of previous longest prefix and suffix
		i = 1
		while i < len(s):
			if s[i] == s[l]:
				lps[i] = l + 1
				l += 1 # increase by 1
				i += 1
			else:
				# if i at the last index
				if l != 0:
					l = lps[l - 1]
				else:
					lps[i] = 0
					i += 1
		return lps[n - 1]
