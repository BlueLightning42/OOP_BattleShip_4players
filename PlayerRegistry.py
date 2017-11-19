"""Player registry module."""

#  Basically I'm stupid and decided global variables in a module is better than a singleton class with a bunch of class methods.
#  And surpisingly stack overflow wasn't a help cause I look into creating singletons and I get sent into global variables in modules
#  then I attempt to search up global variables to treat my module like a singleton class and get all the expected global variables are bad.
#  ahhhhhhhhh only writing this cause I don't think anyone will ever read it.
from random import randint

class registry:
	"""Registry to keep track of gamestate."""

	stats = []
	distroyed_counter = 1
	all_players = []
	total_ship_cells = 0
	SIZE = 8
	players_alive = 4
	all_posible_boats = [5,4,3,3,2]
	def __init__(self, size, boats, players):
		"""Set up all the values that will be treated as constants for a single game."""
		self.SIZE = size
		self.all_posible_boats = boats
		self.total_ship_cells = sum(boats)
		self.players_alive = players

	def hit(self, victim, attacker, has_hit_ship):
		"""Store all information about hit and add bad influence to the attacker."""
		self.all_players(attacker).hits[victim] += 1
		if has_hit_ship:
			self.all_players(attacker).ship_hits[victim] += 1
			self.all_players(attacker).bad_influence[victim] += 10
			self.all_players(victim).bad_influence[attacker] -= 5
		else:
			self.all_players(attacker).bad_influence[victim] += 3
			self.all_players(victim).bad_influence[attacker] -= 1

	def pick_oponent(self, attacker):
		"""Function called by Ai to chose who to attack."""
		chosen_victim = 0  # Attack the user by default
		highest_influence = 0

		for victim in range(len(self.all_players)):
			if victim is attacker: continue  # No self attacks
			#  How annoyied an ai is at someone and how much of a threat they pose
			if self.all_players(attacker).bad_influence[victim] + (self.total_ship_cells - self.all_players(victim).ship_cells_left)*3 + randint(-10, 10) > highest_influence:
				highest_influence = self.all_players(attacker).bad_influence[victim]
				chosen_victim = victim

		return chosen_victim

	def kill_player(self, player_number):
		"""Function called to add stats and remove the ability to attack player."""
		player_number += 1  # Display each player with an offset so there is no player0
		self.players_alive -= 1

		if self.players_alive == 0:
			temp_str = "\nPlayer{} was the last distroyed\n".format(player_number)
		elif self.distroyed_counter == 1:
			temp_str = "\nPlayer{} was the first distroyed\n".format(player_number)
		elif self.distroyed_counter == 2:
			temp_str = "Player{} was the second distroyed\n".format(player_number)
		elif self.distroyed_counter == 3:
			temp_str = "Player{} was the third distroyed\n".format(player_number)
		else:
			temp_str = "Player{} was the {}th distroyed\n".format(player_number, self.distroyed_counter)
		self.distroyed_counter += 1

		for p in range(len(self.all_players)):
			temp_str.append("They hit Player{} {} times\n".format(p, self.all_players(player_number).hits[p]))
			temp_str.append("and were hit by Player{} {} times\n".format(p, self.all_players(p).hits[player_number]))
			self.all_players(p).bad_influence[player_number] = -100  # Remove them from being chosen

		self.stats.append[temp_str]

	def display_stats(self):
		"""At the end of the game function is called to write stats."""
		fileWriter = open("BattleShip_Stats.txt", "w")
		fileWriter.write("".join(sorted(self.stats)))
		fileWriter.close()
