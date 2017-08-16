#Main file 

import player

set_up();
main_loop();
end_program();

#currently using placeholder names for planned functions may change at future points
all_players = []

def set_up():
	#change default size and num?
	SIZE = 8
	NUMBER_OF_PLAYERS = 4

	all_players.append(User(1))
	for bot in range(2, NUMBER_OF_PLAYERS):
		all_players.append(AI(bot, SIZE, NUMBER_OF_PLAYERS))
	#figure out how to draw a gameboard (tkinter?)
	
		
def main_loop():
	while len(all_players) > 1:
	for p in all_players:
		p.attack(all_players)
	
	
def end_program():	
	#write stats?
	#show game over screen?
	pass
