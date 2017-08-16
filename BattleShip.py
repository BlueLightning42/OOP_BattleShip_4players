#Main file 

import Player
import ShipBoard

#set up all players
all_players = set_up();
#play game
main_loop();
#terminate
end_program();

#currently using placeholder names for planned functions may change at future points


def set_up():
	#change default size and num?
	SIZE = 8
	NUMBER_OF_PLAYERS = 4
	
	#looks suspiciously like the factory pattern...hmmmm is this unpythonic?
	all_players = [User(1)]
	for bot in range(2, NUMBER_OF_PLAYERS):
		all_players.append(AI(bot, SIZE, NUMBER_OF_PLAYERS))
	#figure out how to draw a gameboard (tkinter?)
	return all_players
		
def main_loop():
	while len(all_players) > 1:
	for p in all_players:
		p.attack(all_players)
		#update game board?
	
	
def end_program():	
	#write stats?
	#show game over screen?
	pass
