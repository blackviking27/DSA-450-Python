# Find the string in grid 

class Solution:
	def find(self, grid, row, column, word):
		# if the first character doesn't match then move to the next row, column poistion
		if grid[row][column] != word[0]:
			return False

		# searching in all 8 directions
		for x, y in self.dir:
			# initialise the direction
			rd, cd = row + x, column + y
			flag = True
			# finding the reamining characters
			for k in range(1, len(word)):
				if 0 <= rd < self.R and 0 <= cd < self.C and word[k] == grid[rd][cd]:
					# moving in the same direction
					rd += x
					cd += y
				else:
					flag = False
					break
			# found the word in this direction
			if flag:
				return True
		return False
			

	def searchWord(self, grid, word):
		self.R = len(grid) # total number of rows
		self.C = len(grid[0]) # total number of clumns
		# the eight possible directions
		self.dir = [[-1, 0], [1, 0], [1, 1],[1, -1], 
					[-1, -1], [-1, 1], [0, 1], [0, -1]] 
		res = []
		for row in range(self.R):
			for column in range(self.C):
				if self.find(grid, row, column, word): # finding if the word exists in the grid
					res.append([row, column])
		return res