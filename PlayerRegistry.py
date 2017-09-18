"""Player registry module."""

#  Basically I'm stupid and decided global variables in a module is better than a singleton class with a bunch of class methods.
#  And surpisingly stack overflow wasn't a help cause I look into creating singletons and I get sent into global variables in modules
#  then I attempt to search up global variables to treat my module like a singleton class and get all the expected global variables are bad.
#  ahhhhhhhhh only writing this cause I don't think anyone will ever read it.
from random import randint

#  Is this even more stupid? Do I not need to initialize the lists outside of the function first?
stats = []
distroyed_counter = 1
SIZE = 8
players_alive = 4
all_players = []
total_ship_cells = 0
all_posible_boats = [5,4,3,3,2]


def hit(victim, attacker, has_hit_ship):
	"""Store all information about hit and add bad influence to the attacker."""
	all_players(attacker).hits[victim] += 1
	if has_hit_ship:
		all_players(attacker).ship_hits[victim] += 1
		all_players(attacker).bad_influence[victim] += 10
		all_players(victim).bad_influence[attacker] -= 5
	else:
		all_players(attacker).bad_influence[victim] += 3
		all_players(victim).bad_influence[attacker] -= 1

def pick_oponent(attacker):
	"""Function called by Ai to chose who to attack"""
	chosen_victim = 0  # Attack the user by default
	highest_influece = 0

	for victim in range(len(all_players)):
		if victim is attacker: continue  # No self attacks

		#  How annoyied an ai is at someone and how much of a threat they pose
		if all_players(attacker).bad_influence[victim] + (total_ship_cells - all_players(victim).ship_cells_left)*3 + randint(-10, 10) > highest_influence:

			highest_influece = all_players(attacker).bad_influence[victim]
			chosen_victim = victim

	return chosen_victim

def kill_player(player_number):
	global stats, distroyed_counter, players_alive
	player_number += 1  # Display each player with an offset so there is no player0
	players_alive -= 1

	if players_alive == 0:
		temp_str = "\nPlayer{} was the last distroyed\n".format(player_number)
	elif distroyed_counter == 1:
		temp_str = "\nPlayer{} was the first distroyed\n".format(player_number)
	elif distroyed_counter == 2:
		temp_str = "Player{} was the second distroyed\n".format(player_number)
	elif distroyed_counter == 3:
		temp_str = "Player{} was the third distroyed\n".format(player_number)
	else:
		temp_str = "Player{} was the {}th distroyed\n".format(player_number, distroyed_counter)
	distroyed_counter += 1

	for p in range(len(hits)):
		temp_str.append("They hit Player{} {} times\n".format(p, all_players(player_number).hits[p]))
		temp_str.append("and were hit by Player{} {} times\n".format(p, all_players(p).hits[player_number]))
		all_players(p).bad_influence[player_number] = -100  # Remove them from being chosen

	stats.append[tempt_str]

def display_stats():
	fileWriter = open("BattleShip_Stats.txt", w)
	fileWriter.write("".join(sorted(stats)))
	fileWriter.close()
