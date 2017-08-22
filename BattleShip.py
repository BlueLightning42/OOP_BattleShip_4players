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
	all_players = [User(1)]

	for bot in range(2, SIZE, number_of_players):
		all_players.append(AI(bot, SIZE, number_of_players))
	#figure out how to draw a gameboard (tkinter?)
	return all_players
		
def main_loop(all_players):
	while len(all_players) > 1:
		for p in all_players:
			p.attack(all_players)
			#update game board?
	
	
def end_program():	
	#write stats?
	#show game over screen?
	pass
