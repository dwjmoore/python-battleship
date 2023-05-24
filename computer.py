import random


class Computer:

	def __init__(self):
		self.player_number = 2
		self.sunk_ships = 0
		self.attack_coord_log = []
		self.attack_hit_log = []
		self.attack_number = 0
		self.just_sunk_ship = False
		self.found_ship = False

	def attack(self, enemy_ships_board, player_enemy_board, enemy_ships, enemy_player):
		print("Player 2 attacks:")
		self.attack_number += 1
		#Computer inputs attack coordinate
		attack_coord = self.get_attack_coord(player_enemy_board)
		#Checks if attack coord is valid
		attack_coord_valid = self.check_attack_coord_validity(
		 attack_coord, player_enemy_board)
		while attack_coord_valid == False:
			attack_coord = self.get_attack_coord(player_enemy_board)
			attack_coord_valid = self.check_attack_coord_validity(
			 attack_coord, player_enemy_board)
		#Checks attack coord result
		attack_coord_hit = self.check_attack_coord_hit(attack_coord,
		                                               enemy_ships_board)
		#Applies attack coord result to the player boards (and ship if a hit)
		#Appends attack coord result to attack_coord_log and attack_hit_log
		if attack_coord_hit == True:
			enemy_ships_board[attack_coord] = 'X'
			player_enemy_board[attack_coord] = 'X'
			self.add_X_to_ship_and_check_if_sunk(attack_coord, enemy_ships,
			                                     enemy_player)
			self.attack_coord_log.append(attack_coord)
			self.attack_hit_log.append(True)
		if attack_coord_hit == False:
			enemy_ships_board[attack_coord] = 'O'
			player_enemy_board[attack_coord] = 'O'
			self.attack_coord_log.append(attack_coord)
			self.attack_hit_log.append(False)

	def place_ships(self, board, ships):
		print(f"Player {self.player_number} is placing ships.")
		for ship in ships:
			coord1, coord2 = Computer.input_coords(ship, board.player_board)
			Computer.insert_coords_into_player_board(board.player_board, coord1, coord2,
			                                         ship)

	def get_attack_coord(self, player_enemy_board):
		letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

		if self.attack_number == 1 or self.just_sunk_ship == True:
			self.just_sunk_ship = False
			return (random.choice(letters) + random.choice(numbers))

		if self.attack_number >= 3 and self.attack_hit_log[-1] == True and self.attack_hit_log[-2] == True and self.found_ship == True:
			return self.get_attack_coord_after_two_hits()

		if self.attack_number >= 2 and self.attack_hit_log[-1] == True:
			return self.get_attack_coord_after_hit(-1, player_enemy_board)
		if self.attack_number >= 3 and self.attack_hit_log[
		  -1] == False and self.attack_hit_log[
		   -2] == True and self.found_ship == True:
			return self.get_attack_coord_after_hit(-2, player_enemy_board)
		if self.attack_number >= 4 and self.attack_hit_log[
		  -1] == False and self.attack_hit_log[-2] == False and self.attack_hit_log[
		   -3] == True and self.found_ship == True:
			return self.get_attack_coord_after_hit(-3, player_enemy_board)
		if self.attack_number >= 5 and self.attack_hit_log[
		  -1] == False and self.attack_hit_log[-2] == False and self.attack_hit_log[
		   -3] == False and self.attack_hit_log[-4] and self.found_ship == True:
			return self.get_attack_coord_after_hit(-4, player_enemy_board)
		return (random.choice(letters) + random.choice(numbers))

	def check_attack_coord_validity(self, coord, player_enemy_board):
		if player_enemy_board[coord] == 'X' or player_enemy_board[coord] == 'O':
			return False
		return True

	def check_attack_coord_hit(self, attack_coord, enemy_ships_board):
		if bool(enemy_ships_board[attack_coord]) == True:
			print(f"{attack_coord} is a hit!")
			self.found_ship = True
			return True
		print(f"{attack_coord} is a miss.")
		return False

	def add_X_to_ship_and_check_if_sunk(self, attack_coord, enemy_ships, enemy_player):
		for ship in enemy_ships:
			for coord in ship.location:
				if coord == attack_coord:
					ship.location[ship.location.index(attack_coord)] = 'X'
					if ship.check_if_sunk(enemy_player) == True:
						enemy_player.sunk_ships += 1
						self.just_sunk_ship = True
						self.found_ship = False

	def input_coords(ship, player_board):
		letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
		coord1 = (random.choice(letters) + random.choice(numbers))
		coord1_valid = Computer.check_coord1_validity(coord1, player_board)
		while coord1_valid == False:
			coord1 = (random.choice(letters) + random.choice(numbers))
			coord1_valid = Computer.check_coord1_validity(coord1, player_board)

		coord2 = (random.choice(letters) + random.choice(numbers))
		coord2_valid = Computer.check_coord2_validity(coord1, coord2, player_board,
		                                              ship)

		while coord2_valid == False:
			coord2 = (random.choice(letters) + random.choice(numbers))
			coord2_valid = Computer.check_coord2_validity(coord1, coord2, player_board,
			                                              ship)
		return coord1, coord2

	def check_coord1_validity(coord1, player_board):
		#Checks if there is already a ship at the coord entered
		if bool(player_board[coord1]) == True:
			return False
		return True

	def check_coord2_validity(coord1, coord2, player_board, ship):
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
			coords_length = abs(ord(coord1[0]) - ord(coord2[0])) + 1
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
		if coord1[0] != coord2[0] and coord1[0] < coord2[0]:
			for x in range(1, ship.length - 1):
				if bool(player_board[chr(ord(coord1[0]) + x) + coord1[1:]]) == True:
					return False
		if coord1[0] != coord2[0] and coord1[0] > coord2[0]:
			for x in range(1, ship.length - 1):
				if bool(player_board[chr(ord(coord2[0]) + x) + coord2[1:]]) == True:
					return False
		return True

	def insert_coords_into_player_board(player_board, coord1, coord2, ship):
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
		if coord1[0] != coord2[0] and coord1[0] < coord2[0]:
			for x in range(1, ship.length - 1):
				player_board[chr(ord(coord1[0])+ x) + coord1[1:]] = ship.symbol
				ship.location.append(chr(ord(coord1[0]) + x) + coord1[1:])
		if coord1[0] != coord2[0] and coord1[0] > coord2[0]:
			for x in range(1, ship.length - 1):
				player_board[chr(ord(coord2[0]) + x) + coord2[1:]] = ship.symbol
				ship.location.append(chr(ord(coord2[0]) + x) + coord2[1:])

	def get_attack_coord_after_hit(self, element, player_enemy_board):
		letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
		last_hit_coord_letter = self.attack_coord_log[element][0]
		last_hit_coord_number = int(self.attack_coord_log[element][1:])
		attack_coord_options = []
		#Gets attack coord option along the row
		if last_hit_coord_letter == 'A':
			attack_coord_options.append('B' + str(last_hit_coord_number))
		elif last_hit_coord_letter == 'J':
			attack_coord_options.append('I' + str(last_hit_coord_number))
		else:
			attack_coord_options.append(chr(ord(last_hit_coord_letter) - 1) + str(last_hit_coord_number))
			attack_coord_options.append(chr(ord(last_hit_coord_letter) + 1) + str(last_hit_coord_number))
		#Gets attack coord option along the column
		if last_hit_coord_number == 1:
			attack_coord_options.append(last_hit_coord_letter + str(last_hit_coord_number + 1))
		elif last_hit_coord_number == 10:
			attack_coord_options.append(last_hit_coord_letter + str(last_hit_coord_number - 1))
		else:
			attack_coord_options.append(last_hit_coord_letter + str(last_hit_coord_number - 1))
			attack_coord_options.append(last_hit_coord_letter + str(last_hit_coord_number + 1))
		#Selects random attack coord if surrounding coords already attacked
		if len(attack_coord_options) == 2 and (
			player_enemy_board[attack_coord_options[0]] == 'X'
			or player_enemy_board[attack_coord_options[0]]
			== 'O') and (player_enemy_board[attack_coord_options[1]] == 'X'
									 or player_enemy_board[attack_coord_options[1]] == 'O'):
			return (random.choice(letters) + random.choice(numbers))
		if len(attack_coord_options) == 3 and (
			player_enemy_board[attack_coord_options[0]] == 'X'
			or player_enemy_board[attack_coord_options[0]]
			== 'O') and (player_enemy_board[attack_coord_options[1]] == 'X'
									 or player_enemy_board[attack_coord_options[1]] == 'O') and (
										player_enemy_board[attack_coord_options[2]] == 'X'
										or player_enemy_board[attack_coord_options[2]] == 'O'):
			return (random.choice(letters) + random.choice(numbers))
		if len(attack_coord_options) == 4 and (
			player_enemy_board[attack_coord_options[0]] == 'X'
			or player_enemy_board[attack_coord_options[0]]
			== 'O') and (player_enemy_board[attack_coord_options[1]] == 'X'
									 or player_enemy_board[attack_coord_options[1]] == 'O') and (
										player_enemy_board[attack_coord_options[2]] == 'X'
										or player_enemy_board[attack_coord_options[2]] == 'O') and (
										 player_enemy_board[attack_coord_options[3]] == 'X'
										 or player_enemy_board[attack_coord_options[3]] == 'O'):
			return (random.choice(letters) + random.choice(numbers))
		#Randomly gets attack coord from attack coord options list
		return random.choice(attack_coord_options)

	def get_attack_coord_after_two_hits(self):
		first_hit_coord_letter = self.attack_coord_log[-2][0]
		first_hit_coord_number = int(self.attack_coord_log[-2][1:])
		second_hit_coord_letter = self.attack_coord_log[-1][0]
		second_hit_coord_number = int(self.attack_coord_log[-1][1:])
		if first_hit_coord_letter == second_hit_coord_letter:
			if second_hit_coord_number == 1:
				return (first_hit_coord_letter + str(first_hit_coord_number + 1))
			if second_hit_coord_number == 10:
				return (first_hit_coord_letter + str(first_hit_coord_number - 1))
			if first_hit_coord_number > second_hit_coord_number:
				return (first_hit_coord_letter + str(second_hit_coord_number - 1))
			if first_hit_coord_number < second_hit_coord_number:
				return (first_hit_coord_letter + str(second_hit_coord_number + 1))
		if first_hit_coord_number == second_hit_coord_number:
			if second_hit_coord_letter == 'A':
				return (chr(ord(first_hit_coord_letter) + 1) + str(first_hit_coord_number))
			if second_hit_coord_letter == 'J':
				return (chr(ord(first_hit_coord_letter) - 1) + str(first_hit_coord_number))
			if first_hit_coord_letter > second_hit_coord_letter:
				return (chr(ord(second_hit_coord_letter) - 1) + str(first_hit_coord_number))
			if first_hit_coord_letter < second_hit_coord_letter:
				return (chr(ord(second_hit_coord_letter) + 1) + str(first_hit_coord_number))