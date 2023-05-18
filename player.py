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
		coord1_valid = Player.check_coord1_validity(coord1)

		while coord1_valid == False:
			coord1 = input(
			 "Invalid entry. Please enter a letter from A through J and a number from 1 through 10. For example, C3 or D10: "
			).upper().strip()
			coord1_valid = Player.check_coord1_validity(coord1)

		coord2 = input(
		 f"Where would you like to place the other end of your {ship.type}? Enter one coordinate. Ships cannot be placed diagonally, only vertically or horizontally: "
		).upper().strip()
		coord2_valid = Player.check_coord2_validity(coord1, coord2, ship.length)

		while coord2_valid == False:
			coord2 = input(
			 "Invalid entry. Either you entered an invalid coordinate or you tried to place the ship diagonally. Please try again: "
			).upper().strip()
			coord2_valid = Player.check_coord2_validity(coord1, coord2, ship.length)

		return coord1, coord2

	def check_coord1_validity(coord1):
		#Check if the coord entered is a valid letter/number combo
		letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
		coord_letter = coord1[0:1]
		coord_number = coord1[1:]
		if coord_letter not in letters or coord_number:
			return False

		#Check if there is already a ship at that coord entered

		return True



		
		

	def check_coord2_validity(coord1, coord2, ship_length):
		#Check if the coord entered is a valid letter/number combo
		#Check if there is already a ship at that coord entered
		#Check if the length between coords equals ship length
		#check if there is a ship already between coord1 and coord2

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
