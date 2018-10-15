
class Solution(object):
	def bomb(self, grid):
		max_enemy = 0
		for y in range(len(grid)):
			for x in range(len(grid[0])):
				if self.killenemy(grid, x, y) > max_enemy:
					max_enemy = self.killenemy(grid, x, y)
		return max_enemy

	def killenemy(self, grid, x, y):
		countofkillenemy = 0
		for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
			if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid) and grid[y2][x2] != 'W':
				if grid[y2][x2] == 'E': 
					countofkillenemy += 1
		return countofkillenemy

grid = [['0', 'E', '0', '0'],
		['E', '0', 'W', 'E'],
		['0', 'E', '0', '0']]

print(Solution().bomb(grid))