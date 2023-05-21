import random


class Computer:

	def __init__(self):
		self.player_number = 2
		self.sunk_ships = 0

	def attack(self, enemy_ships_board, player_enemy_board, enemy_ships,
	           enemy_player):
		print("Player 2 attacks:")
		#Computer inputs attack coordinate
		letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
		attack_coord = (random.choice(letters) + random.choice(numbers)).strip()
		#Checks if attack coord is valid
		attack_coord_valid = Computer.check_attack_coord_validity(
		 attack_coord, player_enemy_board)
		while attack_coord_valid == False:
			attack_coord = (random.choice(letters) + random.choice(numbers)).strip()
			attack_coord_valid = Computer.check_attack_coord_validity(
			 attack_coord, player_enemy_board)
		#Checks attack coord result
		attack_coord_hit = Computer.check_attack_coord_hit(attack_coord,
		                                                   enemy_ships_board)
		#Applies attack coord result to the player boards (and ship if a hit)
		if attack_coord_hit == True:
			enemy_ships_board[attack_coord] = 'X'
			player_enemy_board[attack_coord] = 'X'
			Computer.add_X_to_ship_and_check_if_sunk(attack_coord, enemy_ships,
			                                         enemy_player)
		if attack_coord_hit == False:
			enemy_ships_board[attack_coord] = 'O'
			player_enemy_board[attack_coord] = 'O'

	def place_ships(self, board, ships):
		print(f"Player {self.player_number} is placing ships.")
		for ship in ships:
			coord1, coord2 = Computer.input_coords(ship, board.player_board)
			Computer.insert_coords_into_player_board(board.player_board, coord1, coord2,
			                                         ship)

	def check_attack_coord_validity(coord, player_enemy_board):
		if player_enemy_board[coord] == 'X' or player_enemy_board[coord] == 'O':
			return False
		return True

	def check_attack_coord_hit(attack_coord, enemy_ships_board):
		if bool(enemy_ships_board[attack_coord]) == True:
			print(f"{attack_coord} is a hit!")
			return True
		print(f"{attack_coord} is a miss.")
		return False

	def add_X_to_ship_and_check_if_sunk(attack_coord, enemy_ships, enemy_player):
		for ship in enemy_ships:
			for coord in ship.location:
				if coord == attack_coord:
					ship.location[ship.location.index(attack_coord)] = 'X'
					if ship.check_if_sunk(enemy_player) == True:
						enemy_player.sunk_ships += 1

	def input_coords(ship, player_board):
		letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
		coord1 = (random.choice(letters) + random.choice(numbers)).strip()
		coord1_valid = Computer.check_coord1_validity(coord1, player_board)
		while coord1_valid == False:
			coord1 = (random.choice(letters) + random.choice(numbers)).strip()
			coord1_valid = Computer.check_coord1_validity(coord1, player_board)

		coord2 = (random.choice(letters) + random.choice(numbers)).strip()
		coord2_valid = Computer.check_coord2_validity(coord1, coord2, player_board,
		                                              ship)

		while coord2_valid == False:
			coord2 = (random.choice(letters) + random.choice(numbers)).strip()
			coord2_valid = Computer.check_coord2_validity(coord1, coord2, player_board,
			                                              ship)
		return coord1, coord2

	def check_coord1_validity(coord1, player_board):
		#Checks if there is already a ship at the coord entered
		if bool(player_board[coord1]) == True:
			return False
		return True

	def check_coord2_validity(coord1, coord2, player_board, ship):
		letters_to_numbers = {
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
		numbers_to_letters = {
		 1: 'A',
		 2: 'B',
		 3: 'C',
		 4: 'D',
		 5: 'E',
		 6: 'F',
		 7: 'G',
		 8: 'H',
		 9: 'I',
		 10: 'J'
		}
		#Checks if coord2 == coord1
		if coord2 == coord1:
			return False
		#Checks if there is already a ship at the coord entered
		if bool(player_board[coord2]) == True:
			return False
		#Checks if the ship is placed diagonally
		if coord1[0] != coord2[0] and coord1[1:] != coord2[1:]:
			return False
		#Check if the length between coords equals ship length
		if coord1[0] == coord2[0]:
			coords_length = abs(int(coord1[1:]) - int(coord2[1:])) + 1
		if coord1[0] != coord2[0]:
			coords_length = abs(letters_to_numbers[coord1[0]] -
			                    letters_to_numbers[coord2[0]]) + 1
		if coords_length < ship.length:
			return False
		if coords_length > ship.length:
			return False
		#Check if there is a ship already between coord1 and coord2
		if coord1[0] == coord2[0] and int(coord1[1:]) < int(coord2[1:]):
			for x in range(1, ship.length - 1):
				if bool(player_board[coord1[0] + str(int(coord1[1:]) + x)]) == True:
					return False
		if coord1[0] == coord2[0] and int(coord1[1:]) > int(coord2[1:]):
			for x in range(1, ship.length - 1):
				if bool(player_board[coord2[0] + str(int(coord2[1:]) + x)]) == True:
					return False
		if coord1[0] != coord2[0] and letters_to_numbers[
		  coord1[0]] < letters_to_numbers[coord2[0]]:
			for x in range(1, ship.length - 1):
				if bool(
				  player_board[numbers_to_letters[letters_to_numbers[coord1[0]] + x] +
				               coord1[1:]]) == True:
					return False
		if coord1[0] != coord2[0] and letters_to_numbers[
		  coord1[0]] > letters_to_numbers[coord2[0]]:
			for x in range(1, ship.length - 1):
				if bool(
				  player_board[numbers_to_letters[letters_to_numbers[coord2[0]] + x] +
				               coord2[1:]]) == True:
					return False
		return True

	def insert_coords_into_player_board(player_board, coord1, coord2, ship):
		letters_to_numbers = {
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
		numbers_to_letters = {
		 1: 'A',
		 2: 'B',
		 3: 'C',
		 4: 'D',
		 5: 'E',
		 6: 'F',
		 7: 'G',
		 8: 'H',
		 9: 'I',
		 10: 'J'
		}
		#Inputs ship symbols into coord1 and coord2
		player_board[coord1] = ship.symbol
		player_board[coord2] = ship.symbol
		#Inputs coord1 and coord2 into ship location array
		ship.location.append(coord1)
		ship.location.append(coord2)
		#Fills in the coordinates between coord1 and coord2 with ship symbols
		#and also inputs them into the ship location array
		if coord1[0] == coord2[0] and int(coord1[1:]) < int(coord2[1:]):
			for x in range(1, ship.length - 1):
				player_board[coord1[0] + str(int(coord1[1:]) + x)] = ship.symbol
				ship.location.append(coord1[0] + str(int(coord1[1:]) + x))
		if coord1[0] == coord2[0] and int(coord1[1:]) > int(coord2[1:]):
			for x in range(1, ship.length - 1):
				player_board[coord2[0] + str(int(coord2[1:]) + x)] = ship.symbol
				ship.location.append(coord2[0] + str(int(coord2[1:]) + x))
		if coord1[0] != coord2[0] and letters_to_numbers[
		  coord1[0]] < letters_to_numbers[coord2[0]]:
			for x in range(1, ship.length - 1):
				player_board[numbers_to_letters[letters_to_numbers[coord1[0]] + x] +
				             coord1[1:]] = ship.symbol
				ship.location.append(numbers_to_letters[letters_to_numbers[coord1[0]] +
				                                        x] + coord1[1:])
		if coord1[0] != coord2[0] and letters_to_numbers[
		  coord1[0]] > letters_to_numbers[coord2[0]]:
			for x in range(1, ship.length - 1):
				player_board[numbers_to_letters[letters_to_numbers[coord2[0]] + x] +
				             coord2[1:]] = ship.symbol
				ship.location.append(numbers_to_letters[letters_to_numbers[coord2[0]] +
				                                        x] + coord2[1:])
