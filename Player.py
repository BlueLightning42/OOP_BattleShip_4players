#player class including both the ai and the user
import random
HIT = True
MISS = False
EMPTY = None
SHIP = True
DIRRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

class Player:
	'''abstract base class'''
	def __init__(self, player_number):
		self.LARGEST_BOAT = 5
		self.boats_left = 5
		self.player_number = player_number
		self.size = SIZE
		
		#Initializes a game board
		self.ocean_board = [[MISS for i in range(size+2)] if (not x or not (size-x+1)) else [MISS if (not i or not (size-i+1)) else EMPTY for i in range(size+2)] for x in range(size+2)]
		
		#Initialise the Empty secret ship board
		self._ship_board = [[MISS for i in range(size)] for x in range(size)]
		
		
	def guess(self):
		#random unoptimal guess (making a stupid ai?)
		while true:
			row,cell = randint(1, SIZE), randint(1, SIZE);
			if self.ocean_board[row][cell] is EMPTY:
				return row,cell
	
	#Don't know if this works yet...I haven't tested it but in theory it should be beautiful
	def generate_probability(self):
		best_choice = (1,1) #default to be replaced
		similar_probabilities = []
		higest_probability = 0
		#check each cell
		for row in range(1,size-1):
			for cell in range(1,size-1):
				#skip cells that are already hit
				if self.ocean_board[row][cell] == HIT: continue
				
				probability=0
				#check in a direction
				def look_dir(direc, row_, cell_):
					prob = 0
					for j in range(1, LARGEST_BOAT):
						if ocean_board[row_ + direc[0]*j][cell_ + direc[1]*j] is EMPTY:
							prob += (LARGEST_BOAT+1-j)
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
		best_choice = random.choice(similar_probabilities)
		return best_choice
	
	def search(self):
		#if player is hit search
		pass
	
	def hit(self, x, y):
		if self._ship_board[x-1][y-1]:
			self.ocean_board[x-1][y-1] = HIT
			return True
		else:
			self.ocean_board[x-1][y-1] = MISS
			return False
	

class User(Player):
	#Unsure whether I'm doing this right/having the two subclasses initiate a different attack function
	@classmethod
	def attack(cls):
		#get user input for example
		x=1;y=1
		chosen_victim = 2
		
		if all_players[chosen_victim].hit(x,y):
			attack(all_players)

	def __del__(self):
		#Game Over
		#delete all other players
		pass
	
	
class AI(Player):
	@classmethod 
	def attack(cls):
		#chose victim
		if all_players[chosen_victim].damaged():
			x,y = all_players[chosen_victim].generate_probability()
		else:
			x,y = guess(all_players[chosen_victim])
		#recursivly attack again if hit was sucess
		if all_players[chosen_victim].hit(x,y): 
			attack(all_players)
