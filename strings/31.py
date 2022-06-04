def solve(s, i, j, level, temp, res):

	if (i == (j + 1) and level == 5):
		res.append(temp[1:])

	# Digits of a number ranging 0-255 can lie only between
	# 0-3
	k = i
	while(k < i + 3 and k <= j):
		
		ad = s[i: k + 1]

		# Return if string starting with '0' or it is
		# greater than 255.
		if ((s[i] == '0' and len(ad) > 1) or int(ad) > 255):
			return

		# Recursively call for another level.
		solve(s, k + 1, j, level + 1, temp + '.' + ad, res)

		k += 1

# driver code
s = "25525511135"
n = len(s)
ans = []
solve(s, 0, n - 1, 1, "", ans)
for s in ans:
	print(s)
