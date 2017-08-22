#player registry module

# Basically I'm stupid and decided global variables in a module is better than a singleton class with a bunch of class methods.
# And surpisingly stack overflow wasn't a help cause I look into creating singletons and I get sent into global variables in modules
# then I attempt to search up global variables to treat my module like a singleton class and get all the expected global variables are bad.
# ahhhhhhhhh only writing this cause I don't think anyone will ever read it.

# Is this even more stupid? Do I not need to initialize the lists outside of the function first?
hits = []
ship_hits = []
influence = []
stats = []
distroyed_counter = 1
SIZE = 8


def initialize_registry(NUMBER_OF_PLAYERS, size):
	global hits; global ship_hits; global influence; global SIZE
	hits = [[0 for i in range(NUMBER_OF_PLAYERS)] for k in range(NUMBER_OF_PLAYERS)]
	ship_hits = deepcopy(self.hits)
	influence = deepcopy(self.hits)
	SIZE = size
	
def hit(victim, attacker, has_hit_ship):
	global hits; global ship_hits; global influence
	hits[victim][attacker] += 1
	
	if has_hit_ship: 
		ship_hits[victim][attacker] += 1
		influence[victim][attacker] += 10
		influence[victim][attacker] -= 5
	else:
		influence[victim][attacker] += 3
		influence[victim][attacker] -= 1
		
def pick_oponent(attacker):
	chosen_victim = 0
	highest_influece = 0
	
	for victim in range(len(influence)):
		if victim is attacker: continue #no self attacks
		if influence[victim][attacker] + randint(-10, 10) > highest_influence:
			highest_influece = influence[victim][attacker]
			chosen_victim = victim
	return chosen_victim

def kill_player(player_number):
	global stats; global influence
	
	if distroyed_counter == 1:
		temp_str = "\nPlayer{} was the first distroyed\n".format(player_number)
	elif distroyed_counter == 2:
		temp_str = "Player{} was the second distroyed\n".format(player_number)
	elif distroyed_counter == 3:
		temp_str = "Player{} was the third distroyed\n".format(player_number)
	else:
		temp_str = "Player{} was the {}th distroyed\n".format(player_number, distroyed_counter)
	
	for p in range(len(hits));
		temp_str.append("They hit Player{} {} times\n".format(p, hits[p][player_number])
		temp_str.append("and were hit by Player{} {} times\n".format(p, hits[player_number][p])
		influence[p][player_number] = -100 #remove them from being chosen
	
	stats.append[tempt_str]
