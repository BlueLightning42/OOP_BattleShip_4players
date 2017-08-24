#Main file 

from Player import Player, User, Ai
import ShipBoard
import PlayerRegistry
#set up all players
all_players = set_up();
#play game
main_loop(all_players);
#terminate
end_program();

#currently using placeholder names for planned functions may change at future points


def set_up():
	#change default size and num?
	size = 8
	number_of_players = 4
	
	PlayerRegistry.initialize_registry(number_of_players, size)
	#looks suspiciously like the factory pattern...hmmmm is this unpythonic?
	all_players = [User(0)]

	for bot_number in range(1, SIZE):
		all_players.append(AI(bot_number))
	#figure out how to draw a gameboard (tkinter?)
	return all_players


# rlly rlly bad look at that asfk what heck
# probably non PEP-8 too
def main_loop(all_players):
	while PlayerRegistry.players_alive:
		for p in all_players:
			if p.ship_cells_left is not 0:
				p.attack(all_players)
			else:
				p = p.death
	
	
def end_program():	
	PlayerRegistry.write_stats()
	#show game over screen?
	pass
