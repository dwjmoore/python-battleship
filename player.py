class Player:

	def __init__(self, player_number):
		self.player_number = player_number

	def attack(self, other_player):
		pass

	def place_ships(self, board, ships):
		print(f"Player {self.player_number}, please place your ships.")
		board.display_board(board.player_board)
		for ship in ships:
			coord1, coord2 = Player.enter_coords(ship)
			print(coord1)
			print(coord2)

		print()

	def enter_coords(ship):
		coord1 = input(
		 f"Where would you like to place one end of your {ship.type}? Enter one coordinate. For example, C3 or D10: "
		).upper().strip()
		letter_check = coord1[0:1]
		number_check = coord1[1:]

		while letter_check not in [
		  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'
		] or number_check not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
			coord1 = input(
			 "Invalid entry. Please enter a letter from A through J and a number from 1 through 10. For example, C3 or D10: "
			).upper().strip()
			letter_check = coord1[0:1]
			number_check = coord1[1:]

		coord2 = input(
		 f"Where would you like to place the other end of your {ship.type}? Enter one coordinate. Ships cannot be placed diagonally, only vertically or horizontally: "
		).upper().strip()
		letter_check = coord2[0:1]
		number_check = coord2[1:]

		while letter_check not in [
		  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'
		] or number_check not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
			coord2 = input(
			 "Invalid entry. Please enter a letter from A through J and a number from 1 through 10. For example, C3 or D10: "
			).upper().strip()
			letter_check = coord2[0:1]
			number_check = coord2[1:]

		return coord1, coord2
