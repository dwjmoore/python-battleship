class Player:
	def __init__(self, player_number):
		self.player_number = player_number
	
	def attack(self, other_player):
		pass
		
	def place_ships(self, board):
		board.display_board(board.player_board)