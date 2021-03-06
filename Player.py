"""Player class including both the ai and the user."""
from random import randint, choice
from copy import deepcopy
from PlayerRegistry import Registry

HIT = True
MISS = False
EMPTY = None
SHIP = True


DIRRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
class Player:
	"""Abstract base class."""

	def __init__(self, player_number, registry):
		"""Initialize all atributes every player shares."""
		self.LARGEST_BOAT = 5
		self.player_number = player_number
		self.is_hit = False
		self.last_hit = (0,0)
		self.size = registry.size

		# Initializes a game board
		self.ocean_board = [[MISS for i in range(self.size+2)] if (not x or not (self.size-x+1)) else [MISS if (not i or not (self.size-i+1)) else EMPTY for i in range(self.size+2)] for x in range(self.size+2)]

		# Initialise the Empty secret ship board
		self._ship_board = [[MISS for i in range(self.size)] for x in range(self.size)]

		self.ship_cells_left = registry.total_ship_cells

		self.hits = [0 for i in range(players_alive)]
		self.ship_hits = deepcopy(self.hits)
		self.bad_influence = deepcopy(self.hits)

	def guess(self):
		"""Method is so the code doesn't look as mechanical.
		-ocationally have the AI make a radom unoptimal guess
		"""
		while True:
			row,cell = randint(1, self.size), randint(1, self.size)
			if self.ocean_board[row][cell] is EMPTY:
				return row,cell

	# Don't know if this works yet...I haven't tested it but in theory it should be beautiful
	def generate_probability(self):
		"""Method that finds the probability of each tile being a ship.
		Then randomly choses one of those tiles to return
		"""
		best_choice = (1,1)  # default to be replaced
		similar_probabilities = []
		higest_probability = 0

		# check each cell
		for row in range(1, self.size-1):
			for cell in range(1, self.size-1):
				# skip cells that are already hit
				if self.ocean_board[row][cell] is not EMPTY: continue

				probability = 0
				# add bias to middles...fixes distribution
				if self.ocean_board[row+1][cell] is EMPTY and self.ocean_board[row-1][cell] is EMPTY:
					probability += 2
				if self.ocean_board[row][cell+1] is EMPTY and self.ocean_board[row][cell-1] is EMPTY:
					probability += 2

				# check all dirrections
				for j in range(1, self.LARGEST_BOAT):
					if self.ocean_board[row + j][cell] is EMPTY:
						# add a larger probability to closer tiles
						probability += (self.LARGEST_BOAT+1-j)
					# If it finds a cell that has already been hit stop looking.
					else: break
				for j in range(1, self.LARGEST_BOAT):
					if self.ocean_board[row][cell + j] is EMPTY:
						probability += (self.LARGEST_BOAT+1-j)
					else: break
				for j in range(1, self.LARGEST_BOAT):
					if self.ocean_board[row - j][cell] is EMPTY:
						probability += (self.LARGEST_BOAT+1-j)
					else: break
				for j in range(1, self.LARGEST_BOAT):
					if self.ocean_board[row][cell - j] is EMPTY:
						probability += (self.LARGEST_BOAT+1-j)
					else: break

				# decide if stronger probability
				if probability > higest_probability:
					similar_probabilities = [(row,cell)]
					higest_probability = probability
				elif probability == higest_probability:
					similar_probabilities.append((row,cell))

		# then chose which probability to use
		best_choice = choice(similar_probabilities)
		return best_choice

	def search(self):
		"""Method to call if the player has been hit.
		Ai will attempt to search in a line to find the ship.
		"""
		x,y = self.last_hit

		if self.ocean_board[x][y-1] or self.ocean_board[x+1][y] or not (self.ocean_board[x-1][y] and self.ocean_board[x+1][y]):
			# horisontal look
			for p in range(self.LARGEST_BOAT):
				if self.ocean_board[x][y-p] == HIT: continue
				elif self.ocean_board[x][y-p] == EMPTY: return (x,y-p)
			for p in range(self.LARGEST_BOAT):
				if self.ocean_board[x][y+p] == HIT: continue
				elif self.ocean_board[x][y+p] == EMPTY: return (x,y+p)
		elif self.ocean_board[x-1][y] or self.ocean_board[x+1][y] or not (self.ocean_board[x][y-1] and self.ocean_board[x][y+1]):
			# virticle look
			for p in range(self.LARGEST_BOAT):
				if self.ocean_board[x-p][y] == HIT: continue
				elif self.ocean_board[x-p][y] == EMPTY: return (x-p,y)
			for p in range(self.LARGEST_BOAT):
				if self.ocean_board[x+p][y] == HIT: continue
				elif self.ocean_board[x+p][y] == EMPTY: return (x+p,y)

		self.is_hit = False
		return self.generate_probability()

	def hit(self, x, y):
		"""Hit the ocean board as well as return whether it was sucessfull or not."""
		if self._ship_board[x-1][y-1]:
			self.is_hit = True
			self.ship_cells_left -= 1
			self.last_hit = (x,y)

			self.ocean_board[x-1][y-1] = HIT
			return True
		else:
			self.ocean_board[x-1][y-1] = MISS
			return False

	def death(self):
		registry.kill_player(self.player_number)
		return DeadPlayer

class User(Player):
	"""The person playing the game."""

	def __init__(self, player_number):
		super().__init__(player_number)
		# Initialise once the total cells
		registry.total_ship_cells = self.ship_cells_left
		# Get user input from the form.

	def attack(self, chosen_victim, x, y):
		if all_players[chosen_victim].hit(x, y):
			registry.hit(chosen_victim, self.player_number, True)
			all_players[chosen_victim].attack(all_players)
		else:
			registry.hit(chosen_victim, self.player_number, False)

		return self.ship_cells_left == 0


class AI(Player):
	"""Computer the user plays againsed."""

	def __init__(self, player_number):
		super().__init__(player_number)

		# computer chosing where to hide thire boats
		for boat in registry.all_posible_boats:
			while True:
				col,row = randint(1, self.size), randint(1, self.size)
				direction = DIRRECTIONS[randint(0,3)]

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
		"""Method called for every ai instance.
		-will chose who to attack then hit them.
		"""
		chosen_victim = registry.pick_oponent(self.player_number)
		if all_players[chosen_victim].is_hit:
			x,y = all_players[chosen_victim].search()
		else:
			x,y = all_players[chosen_victim].generate_probability()

		if all_players[chosen_victim].hit(x, y):
			registry.hit(chosen_victim, self.player_number, True)
			all_players[chosen_victim].attack(all_players)
		else:
			registry.hit(chosen_victim, self.player_number, False)

		return self.ship_cells_left == 0

class DeadPlayer:
	"""Empty class for dead players."""

	def __init__(self):
		self.ship_cells_left == 0

	def attack(self, all_players):
		return False

	def death(self):
		return self
