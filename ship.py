class Ship:

	def __init__(self, type):
		self.type = type
		if self.type == 'carrier':
			self._length = 5
			self._symbol = 'A'
		if self.type == 'battleship':
			self._length = 4
			self._symbol = 'B'
		if self.type == 'cruiser':
			self._length = 3
			self._symbol = 'C'
		if self.type == 'submarine':
			self._length = 3
			self._symbol = 'S'
		if self.type == 'destroyer':
			self._length = 2
			self._symbol = 'D'
		self._location = []

	def append_placement_coord_to_ship_location(self, coord):
		self._location.append(coord)

	def add_hit_to_ship(self, coord):
		self._location[self._location.index(coord)] = 'X'
	
	def check_if_sunk(self, enemy_player):
		hit_count = 0
		for x in range(self._length):
			if self._location[x] == 'X':
				hit_count += 1
		if hit_count == self._length:
			print(f"Player {enemy_player.player_number}'s {self.type} is sunk.")
			return True
		return False

	def get_ship_location(self):
		return self._location

	def get_ship_length(self):
		return self._length

	def get_ship_symbol(self):
		return self._symbol