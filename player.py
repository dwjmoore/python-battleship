class Player:

	def __init__(self, player_number):
		self.player_number = player_number

	def attack(self, other_player):
		pass

	def place_ships(self, board, ships):
		print(f"Player {self.player_number}, please place your ships.")
		board.display_board(board.player_board)
		for ship in ships:
			coord1, coord2 = Player.input_coords(ship)
			Player.insert_coords_into_player_board(board.player_board, coord1, coord2,
			                                       ship)
			board.display_board(board.player_board)

	def input_coords(ship):
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

		while (letter_check not in [
		  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'
		]) or (number_check not in [
		  '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'
		]) or (coord1[0:1] != coord2[0:1] and coord1[1:] != coord2[1:]):
			coord2 = input(
			 "Invalid entry. Either you entered an invalid coordinate or you tried to place the ship diagonally. Please try again: "
			).upper().strip()
			letter_check = coord2[0:1]
			number_check = coord2[1:]

		Player.is_coord_length_too_long(coord1, coord2, ship.length)
		return coord1, coord2

	def is_coord_length_too_long(coord1, coord2, ship_length):
		letters = {
		 'A': 1,
		 'B': 2,
		 'C': 3,
		 'D': 4,
		 'E': 5,
		 'F': 6,
		 'G': 7,
		 'H': 8,
		 'I': 9,
		 'J': 10
		}
		if coord1[0:1] != coord2[0:1]:
			coords_length = abs(letters[coord1[0:1]] - letters[coord2[0:1]]) + 1
			print(coords_length)

	def insert_coords_into_player_board(board, coord1, coord2, ship):
		if ship.type == 'carrier':
			board[coord1] = 'A'
			board[coord2] = 'A'
		if ship.type == 'battleship':
			board[coord1] = 'B'
			board[coord2] = 'B'
		if ship.type == 'cruiser':
			board[coord1] = 'C'
			board[coord2] = 'C'
		if ship.type == 'submarine':
			board[coord1] = 'S'
			board[coord2] = 'S'
		if ship.type == 'destroyer':
			board[coord1] = 'D'
			board[coord2] = 'D'
