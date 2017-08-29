#Main file 

from Player import Player, User, Ai
import ShipBoard
import PlayerRegistry
import tkinter as tk

#set up all players
set_up();
#play game
main_loop();
#terminate
end_program();
	

def set_up():
	#change default size and num?
	size = 8
	number_of_players = 4
	if size <= 4:
		Person.all_boats = [2,2]
	elif size == 5:
		Person.all_boats = [4,3,2,2]
	elif size <= 8:
		Person.all_boats = [5,4,3,3,2]
	elif size <= 12:
		Person.all_boats = [7,6,5,5,4,3,3,2]
	else:
		Person.all_boats = [10,7,6,5,5,4,4,3,2,2]
	
	PlayerRegistry.SIZE = size
	PlayerRegistry.players_alive = number_of_players
	PlayerRegistry.total_ship_cells = sum(Person.all_boats)
	
	#Store all the players in the registry
	PlayerRegistry.all_players = [User(0)]

	for bot_number in range(1, SIZE):
		PlayerRegistry.all_players.append(AI(bot_number))


# rlly rlly bad look at that asfk what heck
# probably non PEP-8 too
def process_round(player_clicked, row, cell):
	for p in PlayerRegistry.all_players:
		if p.ship_cells_left is User and p.ship_cells_left is not 0:
			p.attack(player_clicked, row, cell)
		elif p.ship_cells_left is not 0:
			p.attack()
		else:
			p = p.death
			
	if PlayerRegistry.players_alive: return True
	else: return False
	
	
def end_program():	
	PlayerRegistry.write_stats()
	#show game over screen?
	pass
