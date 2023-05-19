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

	def take_a_hit(self):
		pass