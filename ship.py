class Ship:
	def __init__(self, type):
		self.type = type
		if self.type == 'carrier':
			self.length = 5
		if self.type == 'battleship':
			self.length = 4
		if self.type == 'cruiser' or self.type == 'submarine':
			self.length = 3
		if self.type == 'destroyer':
			self.length = 2

	def take_a_hit(self):
		pass