#player class including both the ai and the user
from random import randint, choice
from copy import deepcopy
HIT = True
MISS = False
EMPTY = None
SHIP = True

DIRRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
class Player:
	'''abstract base class'''
	def __init__(self, player_number, SIZE, NUMBER_OF_PLAYERS):
		self.LARGEST_BOAT = 5
		self.boats_left = 5
		self.player_number = player_number
		self.SIZE = SIZE
		
		#Initializes a game board
		self.ocean_board = [[MISS for i in range(size+2)] if (not x or not (self.SIZE-x+1)) else [MISS if (not i or not (self.SIZE-i+1)) else EMPTY for i in range(self.SIZE+2)] for x in range(self.SIZE+2)]
		
		#Initialise the Empty secret ship board
		self._ship_board = [[MISS for i in range(self.SIZE)] for x in range(self.SIZE)]
		
		
	def guess(self):
		#random unoptimal guess (making a stupid ai?)
		while True:
			row,cell = randint(1, self.SIZE), randint(1, self.SIZE);
			if self.ocean_board[row][cell] is EMPTY:
				return row,cell
	
	#Don't know if this works yet...I haven't tested it but in theory it should be beautiful
	def generate_probability(self):
		best_choice = (1,1) #default to be replaced
		similar_probabilities = []
		higest_probability = 0
		#check each cell
		for row in range(1, self.SIZE-1):
			for cell in range(1, self.SIZE-1):
				#skip cells that are already hit
				if self.ocean_board[row][cell] == HIT: continue
				
				probability=0
				#check in a direction
				def look_dir(direc, row_, cell_):
					prob = 0
					for j in range(1, self.LARGEST_BOAT):
						if self.ocean_board[row_ + direc[0]*j][cell_ + direc[1]*j] is EMPTY:
							prob += (self.LARGEST_BOAT+1-j)
						else: break
					return prob
				
				look_dir(DIRRECTIONS[0], row, cell) #up
				look_dir(DIRRECTIONS[1], row, cell) #down
				look_dir(DIRRECTIONS[2], row, cell) #left
				look_dir(DIRRECTIONS[3], row, cell) #right

				#decide if stronger probability
				if probability > higest_probability:
					similar_probabilities = [(row,cell)]
					higest_probability = probability
				elif probability == higest_probability:
					similar_probabilities.append((row,cell))

		#then chose which probability to use
		best_choice = choice(similar_probabilities)
		return best_choice
	
	def search(self):
		#if player is hit search
		pass
	
	def hit(self, x, y, attacker):
		if self._ship_board[x-1][y-1]:
			self.ocean_board[x-1][y-1] = HIT
			return True
		else:
			self.ocean_board[x-1][y-1] = MISS
			self.regestry[attacker][2] +=3
			return False
	

class User(Player):
	#Unsure whether I'm doing this right/having the two subclasses initiate a different attack function
	def attack(self):
		#get user input for example
		x=1;y=1
		chosen_victim = player_regestry
		
		if all_players[chosen_victim].hit(x,y):
			all_players[chosen_victim].attack()

	def __del__(self):
		#Game Over
		#delete all other players
		pass
	
	
class AI(Player):
	
	#Fixed it I think?
	def __init__(self, player_number, SIZE, NUMBER_OF_PLAYERS):
		
		super().__init__(player_number, SIZE, NUMBER_OF_PLAYERS)
		self._ship_board = [[MISS for i in range(self.SIZE)] for x in range(self.SIZE)]
		#standard set up
		all_boats = [5,4,3,3,2]
		for boat in all_boats:
			while True:
				col,row = randint(1, self.SIZE), randint(1, self.SIZE);
				direction = DIRRECTIONS[randint(0,1)]
				
				if self.validate_direction(col, row, boat, direction): 
					self.fill_direction(col, row, boat, direction)
					break

	def validate_direction(self, col, row, length, direction):
		try:
			for i in range(length):
				if self._ship_board[col + i*direction[0]][row + i*direction[1]] == SHIP: return False
		except IndexError:
			return False
		return True
		
	def fill_direction(self, col, row, length, direction):
		for i in range(length):
			self._ship_board[col + i*direction[0]][row + i*direction[1]] = SHIP
	
	def attack(self):
		chosen_victim = PlayerRegestry.pick_oponent(self.player_number):
		
		if all_players[chosen_victim].hit(x, y, self.player_number):
			all_players[chosen_victim].attack(all_players)
			
#####################################################################################################################
# maybe I'm being stupid but this seemed like the best way to bundle a bunch of variables and funcitons to acess them
# even tho its a singleton...should I have looked more into what modules are?
class PlayerRegestry:
	def __init__(self, size):
		self.hits = [[0 for i in range(NUMBER_OF_PLAYERS)] for k in range(NUMBER_OF_PLAYERS)]
		self.ship_hits = deepcopy(self.hits)
		self.influence = deepcopy(self.hits)
		
	def hit(attacker, victim, has_hit_ship):
		self.hits[victim][attacker] += 1
		if has_hit_ship: 
			self.ship_hits[victim][attacker] += 1
			self.influence[victim][attacker] += 10
		else:
			self.influence[victim][attacker] += 5
			
	def pick_oponent(self, attacker):
		chosen_victim = 0
		highest_influece = 0
		for victim in range(len(self.influence)):
			if victim is attacker: continue #no self attacks
			if self.influence[victim][attacker] + randint(-10, 10) > highest_influence:
				highest_influece = self.influence[victim][attacker]
				chosen_victim = victim
		return chosen_victim
			

				
