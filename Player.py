#player class including both the ai and the user
HIT = True
MISS = False
EMPTY = None
SHIP = True

class Player:
	'''abstract base class'''
	def __init__(self, player_number):
		self.LARGEST_BOAT = 5
		self.boats_left = 5
		self.player_number = player_number
		self.size = SIZE
		
	def guess(self):
		#random unoptimal guess
		pass
	
	def generate_probability(self):
		#smart guessing
		pass
	
	def search(self):
		#if player is hit
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
