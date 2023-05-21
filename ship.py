class Ship:

	def __init__(self, type):
		self.type = type
		if self.type == 'carrier':
			self.length = 5
			self.symbol = 'A'
		if self.type == 'battleship':
			self.length = 4
			self.symbol = 'B'
		if self.type == 'cruiser':
			self.length = 3
			self.symbol = 'C'
		if self.type == 'submarine':
			self.length = 3
			self.symbol = 'S'
		if self.type == 'destroyer':
			self.length = 2
			self.symbol = 'D'
		self.location = []

	def check_if_sunk(self):
		hit_count = 0
		for x in range(self.length):
			if self.location[x] == 'X':
				hit_count += 1
		if hit_count == self.length:
			print(f"You sunk your opponent's {self.type}.")
			return True
		return False
