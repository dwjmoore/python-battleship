class Player:

	def __init__(self, player_number):
		self.player_number = player_number

	def attack(self, other_player):
		pass

	def place_ships(self, board, ships):
		print(f"Player {self.player_number}, please place your ships.")
		board.display_board(board.player_board)

		for ship in ships:
			coord = input(
			 f"Where would you like to place one end of your {ship.type}? Enter one coordinate. For example, C3: "
			)

		print()