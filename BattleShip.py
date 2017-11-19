"""Main file."""

from Player import User, AI, DeadPlayer
import PlayingField
from PlayerRegistry import Registry
# import tkinter as tk

def set_up():
	"""Setup gameboard by gathering user input."""
	# three presets currently input will change to GUI
	prest = int(input("enter preset: (message doesn't matter as it will be removed)"))
	if prest == 1:
		size = 8
		number_of_players = 4
		boats = [5,4,3,3,2]
	elif prest == 2:
		size = 10
		number_of_players = 2
		boats = [5,4,3,3,2]
	elif prest == 3:
		size = 6
		number_of_players = 6
		boats = [4,3,2,2]
	elif prest == 4:
		size = 12
		number_of_players = 3
		boats = [7,6,5,5,4,3,3,2]
	elif prest == 5:
		size = 12
		number_of_players = 3
		boats = [10,7,6,5,5,4,4,3,2,2]
	else:
		size = int(input("size:"))
		number_of_players = int(input("Number of players"))
		boats = list(map(int, input("boat set up in the form '8 7 3'").split(" ")))

	# Store all the players in the registry
	r = Registry(size, boats, number_of_players)

	return r

def process_round(player_clicked, row, cell):
	"""Function Processes a single round with everyone hitting after the user."""
	for p in registry.all_players:
		if p is User and p.ship_cells_left is not 0:
			p.attack(player_clicked, row, cell)
		elif p is AI and p.ship_cells_left is not 0:
			p.attack()
		elif p is not DeadPlayer:
			p = p.death

def end_program(registry):
	"""After ending the program write stats and show game over screen."""
	registry.write_stats()
	# Show game over screen?
	pass


if __name__ == '__main__':
	r = set_up()

	# play game
	root = PlayingField.App(r)
	root.mainloop()

	# write stats at the end of the game
	end_program()
