#Main file 

from Player import Player, User, Ai
import ShipBoard
import PlayerRegistry
import tkinter as tk

def set_up():
	#three presets currently input will change to GUI
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
	elif prest == 5
		size = 12
		number_of_players = 3
		boats = [10,7,6,5,5,4,4,3,2,2]
	else:
		size = int(input("size:"))
		number_of_players = int(input("Number of players"))
		boats =  list(map(int, input("boat set up in the form '8 7 3'").split(" "))
			      
	
	Person.all_boats = boats
	PlayerRegistry.SIZE = size
	PlayerRegistry.players_alive = number_of_players
	PlayerRegistry.total_ship_cells = sum(Person.all_boats)
	
	#Store all the players in the registry
	PlayerRegistry.all_players = [User(0)]

	for bot_number in range(1, SIZE):
		PlayerRegistry.all_players.append(AI(bot_number))


def process_round(player_clicked, row, cell):
	for p in PlayerRegistry.all_players:
		if p.ship_cells_left is User and p.ship_cells_left is not 0:
			p.attack(player_clicked, row, cell)
		elif p.ship_cells_left is not 0:
			p.attack()
		else:
			p = p.death
	
	
def end_program():	
	PlayerRegistry.write_stats()
	#show game over screen?
	pass

if __name__ == '__main__':
	#set up all players
	set_up();
	
	#play game
	root = tk.Tk()
	root.grid()
	for p in all_players:
		player_frame = Grid(p.player_number)
		root.player_frame.pack()
		
	root.mainloop()
	
	#write stats at the end of the game
	end_program();

	

