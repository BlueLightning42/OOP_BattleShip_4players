"""GameBoard and Tileset for use in the gui."""

# To do...absolutly everything starting from how to do gui programming.

from PlayerRegistry import SIZE
import BattleShip
import PlayerRegistry
import os.path
import tkinter as tk

root = tk.Tk()
HIT_img = tk.PhotoImage(os.path.join("images","HIT.jpg"))
MISS_img = tk.PhotoImage(os.path.join("images","MISS.jpg"))
EMPTY_img = tk.PhotoImage(os.path.join("images","EMPTY.jpg"))
# For the user's board
BLANK_img = tk.PhotoImage(os.path.join("images","BLANK.jpg"))
BOAT_img = tk.PhotoImage(os.path.join("images","BOAT.jpg"))

class Tile(tk.Button):
	"""Ocean tile for the player's board."""

	def __init__(self, master, row, cell):
		self.row = row
		self.cell = cell
		tk.Button.__init__(self, master)
		if master.player_number is 0:
			self.config(image=BLANK_img, width="32", height="32", state=tk.DISABLED)
		else:
			self.config(image=EMPTY_img, width="32", height="32", command=lambda row=self.row, cell=self.cell: master.grid_click(row, cell))

	def update(self, has_hit):
		"""Update the state of the grid when ever its hit."""
		if has_hit:
			self.config(mage=HIT_img, state=tk.DISABLED)
		else:
			self.config(image=MISS_img, state=tk.DISABLED)

class OceanGrid(tk.Frame):
	"""Grid for each player."""

	def __init__(self, player_number):
		tk.Frame.__init__(self, width=SIZE*32, height=SIZE*32, bd=1, relief=tk.SUNKEN)  # super()__init__ not working?
		self.player_number = player_number

		self.ocean = [[Tile(self, i, j) for i in range(SIZE)] for j in range(SIZE)]
		for i in range(SIZE):
			for j in range(SIZE):
				self.ocean[i][j].grid(row=i, column=j)

	def grid_click(self, row, cell):
		"""Send the clicked cell to process round."""
		print("Player {}, cord {},{}".format(self.player_number, row+1, cell+1))
		BattleShip.process_round(self.player_number, row+1, cell+1)

	def update(self, row, cell, has_hit):
		"""Update the state of the grid when ever its hit."""
		self.ocean[row-1][cell-1].update(has_hit)

class App(tk.Tk):
	"""Top-this is the main app.  Will be changed once I get the grid to work."""

	def __init__(self, game_state):
		(size, boats, number_of_players) = game_state
		tk.Tk.__init__(self)
		width = int(number_of_players ** 0.5)

		for p in PlayerRegistry.all_players:
			OceanGrid(size, p.player_number).grid(row=p.player_number % width, column=int(p.player_number/2), padx=5, pady=5)


# Testing.
if __name__ == '__main__':

	root = App()
	root.mainloop()
