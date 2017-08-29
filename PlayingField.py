#board.py

#to do...absolutly everything starting from how to do gui programming.

from PlayerRegistry import SIZE
import os.path
import tkinter as tk
import BattleShip

HIT_img = tk.PhotoImage(os.path.join("images","HIT.jpg"))
MISS_img = tk.PhotoImage(os.path.join("images","HIT.jpg"))
EMPTY_img = tk.PhotoImage(os.path.join("images","HIT.jpg"))

class Tile(tk.Button):
	'''ocean tile for the player's board'''
	def __init__(self, master, row, cell, *args, **kwargs):
		self.cord = (row, cell)
		super().__init__(self,command=lambda (row,cell) = self.cord: master.grid_click(row, cell), *args, **kwargs)
		self.config(image=EMPTY_img, width="32", height="32")
		
		
	def update(self, has_hit):
		'''update the state of the grid when ever its hit'''
		if has_hit:
			self.config(image=HIT_img, state = DISABLED)
		else:
			self.config(image=MISS_img, state = DISABLED)
		
class Grid(tk.Frame):
	'''grid for each player'''
	def __init__(self, player_number)
		self.player_number = player_number
		#self.button_grid = [[Tile(i, j) for i in range(SIZE)] for j in range(SIZE)]
		for i in range(SIZE):
			for j in range(SIZE)
				self.ocean[i][j].append(Tile(self, i, j)
			
				
	def grid_click(self, row, cell):
		BattleShip.process_round(self.player_number, row+1, cell+1):
		
	def update(self, row, cell, has_hit):
		'''update the state of the grid when ever its hit'''
		self.ocean[row-1][cell-1].update(has_hit)
