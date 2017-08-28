#board.py

#to do...absolutly everything starting from how to do gui programming.



#main ideas either set up a table for each player that can track which cells are clicked
#OR just set up a 2d array of buttons and figure out how to link them to the "ship_board" list for each player

from PlayerRegistry import SIZE




HIT = True
MISS = False
EMPTY = None

class Tile():
	'''ocean cell for the grid'''
	def __init__(self):
		self.state = EMPTY
		return self
	
	
class Grid():
	'''grid for each player'''
	def __init__(self)
		self.ocean_grid = [[Tile() for i in range(SIZE)] for j in range(SIZE)
		return self
	
	def update_grid(self, row, cell, has_hit):
		if has_hit:
			self.ocean_grid[row+1][cell+1].state = HIT
		else:
			self.ocean_grid[row+1][cell+1].state = MISS
