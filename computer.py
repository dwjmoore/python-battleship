import helpers


class Computer:

	def __init__(self, player_number):
		self.player_number = player_number
		self._sunk_ships = 0
		self._attack_coord_log = []
		self._attack_result_log = []
		self._attack_number = 0
		self._just_sunk_ship = False
		self._found_ship = False

	def attack(self, player_board, enemy_board, enemy_ships, enemy_player):
		self._attack_number += 1
		print(f"Attack # {self._attack_number} -- Player {self.player_number} attacks:")
		attack_coord = self.get_attack_coord()
		attack_coord_valid = helpers.check_attack_coord_validity(attack_coord, player_board)
		while attack_coord_valid == False:
			attack_coord = self.get_attack_coord()
			attack_coord_valid = helpers.check_attack_coord_validity(attack_coord, player_board)
		attack_coord_hit = helpers.check_attack_coord_result(self, attack_coord, enemy_board)
		enemy_board.insert_attack_result_into_board(attack_coord_hit, attack_coord)
		player_board.insert_attack_result_into_radar(attack_coord_hit, attack_coord)
		self.append_attack_coord_and_result(attack_coord, attack_coord_hit)
		if attack_coord_hit == True:
			helpers.add_hit_to_ship_and_check_if_sunk(self, attack_coord, enemy_ships, enemy_player)
			
	def place_ships(self, player_board, ships):
		print(f"Player {self.player_number} is placing ships.")
		for ship in ships:
			coord1, coord2 = self.get_ship_placement_coords(ship, player_board)
			player_board.insert_placement_coords_into_board(coord1, coord2, ship)

	def get_attack_coord(self):
		if self._attack_number == 1 or self._just_sunk_ship == True:
			self.set_just_sunk_ship(False)
			return helpers.get_random_coord()
		self.set_just_sunk_ship(False)
		return helpers.get_random_coord()

	def check_attack_coord_hit(self, attack_coord, enemy_ships_board):
		if bool(enemy_ships_board[attack_coord]) == True:
			print(f"{attack_coord} is a hit!")
			self.found_ship = True
			return True
		print(f"{attack_coord} is a miss.")
		return False

	def get_ship_placement_coords(self, ship, player_board):
		coord1 = helpers.get_random_coord()
		coord1_valid = helpers.check_placement_coord1_validity(coord1, player_board)
		while coord1_valid == False:
			coord1 = helpers.get_random_coord()
			coord1_valid = helpers.check_placement_coord1_validity(coord1, player_board)
		coord2 = helpers.get_random_coord()
		coord2_valid = helpers.check_placement_coord2_validity(coord1, coord2, player_board, ship)
		while coord2_valid == False:
			coord2 = helpers.get_random_coord()
			coord2_valid = helpers.check_placement_coord2_validity(coord1, coord2, player_board, ship)
		return coord1, coord2

	def append_attack_coord_and_result(self, coord, result):
		self._attack_coord_log.append(coord)
		self._attack_result_log.append(result)

	def add_to_sunk_ships(self):
		self._sunk_ships += 1

	def get_sunk_ships(self):
		return self._sunk_ships
	
	def set_just_sunk_ship(self, value):
		self._just_sunk_ship = value

	def set_found_ship(self, value):
		self._found_ship = value