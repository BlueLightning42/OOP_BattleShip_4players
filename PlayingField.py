#board.py

#to do...absolutly everything starting from how to do gui programming.



#main ideas either set up a table for each player that can track which cells are clicked
#OR just set up a 2d array of buttons and figure out how to link them to the "ship_board" list for each player

from PlayerRegistry import SIZE
import os.path
import tkinter as tk


HIT_img = tk.PhotoImage(os.path.join("images","HIT.jpg"))
MISS_img = tk.PhotoImage(os.path.join("images","HIT.jpg"))
EMPTY_img = tk.PhotoImage(os.path.join("images","HIT.jpg"))


class Grid(tk.Frame):
	'''grid for each player'''
	def __init__(self)
		for i in range(SIZE):
			self.button_grid.append([])
			for j in range(SIZE):
				self.buttons[i].append(tk.Button(self, image=EMPTY_img, bg="blue", command=grid_click))
				self.ocean.(row=i, column=j, sticky="nsew")
	def grid_click(self):
		
		pass
		
	def update(self, row, cell, has_hit):
		'''update the state of the grid when ever its hit'''
		if 
		self.ocean_grid[row-1][cell-1].state = has_hit
