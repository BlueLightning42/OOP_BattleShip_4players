"""GameBoard and Tileset for use in the gui"""

#to do...absolutly everything starting from how to do gui programming.

from PlayerRegistry import SIZE
import BattleShip
import os.path
import tkinter as tk

HIT_img = tk.PhotoImage(os.path.join("images","HIT.jpg"))
MISS_img = tk.PhotoImage(os.path.join("images","MISS.jpg"))
EMPTY_img = tk.PhotoImage(os.path.join("images","EMPTY.jpg"))
#for the user's board
BLANK_img = tk.PhotoImage(os.path.join("images","BLANK.jpg"))
BOAT_img = tk.PhotoImage(os.path.join("images","BOAT.jpg"))

class Tile(tk.Button):
	"""Ocean tile for the player's board."""
	def __init__(self, master, row, cell, *args, **kwargs):
		self.cord = (row, cell)
		super().__init__(self, *args, **kwargs)
		if master.player_number is 0:
			self.config(image=BLANK_img, width="32", height="32", state = DISABLED)
		else:
			self.config(image=EMPTY_img, width="32", height="32", command=lambda row, cell = self.cord: master.grid_click(row, cell))

	def update(self, has_hit):
		"""Update the state of the grid when ever its hit."""
		if has_hit:
			self.config(image=HIT_img, state = DISABLED)
		else:
			self.config(image=MISS_img, state = DISABLED)

class Grid(tk.Frame):
	"""Grid for each player."""

	def __init__(self, player_number):
		super().__init__(self, width=SIZE*32, height=SIZE*32, bd=1, relief=Tk.SUNKEN)
		self.player_number = player_number
		#self.button_grid = [[Tile(i, j) for i in range(SIZE)] for j in range(SIZE)]
		for i in range(SIZE):
			for j in range(SIZE):
				self.ocean[i][j].append(Tile(self, i, j))
				self.grid(master=self, fill=self.ocean[i][j], row=i, column=j)

	def grid_click(self, row, cell):
		"""Sends the clicked cell to process round."""
		BattleShip.process_round(self.player_number, row+1, cell+1):

	def update(self, row, cell, has_hit):
		"""Update the state of the grid when ever its hit."""
		self.ocean[row-1][cell-1].update(has_hit)
