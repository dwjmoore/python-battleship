import helpers


class Computer:

	def __init__(self, player_number):
		self._player_number = player_number
		self._sunk_ships = 0
		self._attack_coord_log = []
		self._attack_result_log = []
		self._attack_number = 0
		self._just_sunk_ship = False
		self._found_ship = False

	def attack(self, player_board, enemy_board, enemy_ships, enemy_player):
		self._attack_number += 1
		print(f"Attack # {self._attack_number} -- Player {self._player_number} attacks:")
		attack_coord = self.get_attack_coord(player_board)
		attack_coord_valid = False if attack_coord in self._attack_coord_log else True
		while attack_coord_valid == False:
			attack_coord = self.get_attack_coord(player_board)
			attack_coord_valid = False if attack_coord in self._attack_coord_log else True
		attack_coord_hit = helpers.check_attack_coord_result(self, attack_coord, enemy_board)
		enemy_board.insert_attack_result_into_board(attack_coord_hit, attack_coord)
		player_board.insert_attack_result_into_radar(attack_coord_hit, attack_coord)
		self.insert_attack_coord_and_result(attack_coord, attack_coord_hit)
		if attack_coord_hit == True:
			helpers.add_hit_to_ship_and_check_if_sunk(self, attack_coord, enemy_ships, enemy_player)
			
	def place_ships(self, player_board, ships):
		print(f"Player {self._player_number} is placing ships.")
		for ship in ships:
			coord1, coord2 = self.get_ship_placement_coords(ship, player_board)
			player_board.insert_placement_coords_into_board(coord1, coord2, ship)

	def get_attack_coord(self, player_board):
		if self._found_ship == False:
			self.set_just_sunk_ship(False)
			return helpers.get_random_coord()

		if self._found_ship == True:
			#get location of last hit
			#search around last hit coord for another hit coord
			#get new hit coord
			pass
			
		
		return helpers.get_random_coord()

	def get_ship_placement_coords(self, ship, player_board):
		coord1 = helpers.get_random_coord()
		coord1_valid = False if bool(player_board.get_coord_value_in_board(coord1)) else True
		while coord1_valid == False:
			coord1 = helpers.get_random_coord()
			coord1_valid = False if bool(player_board.get_coord_value_in_board(coord1)) else True
		coord2 = helpers.get_placement_coord2(coord1, ship)
		coord2_valid = helpers.check_placement_coord2_validity(coord1, coord2, player_board, ship)
		while coord2_valid == False:
			coord2 = helpers.get_placement_coord2(coord1, ship)
			coord2_valid = helpers.check_placement_coord2_validity(coord1, coord2, player_board, ship)
		return coord1, coord2

	def insert_attack_coord_and_result(self, coord, result):
		self._attack_coord_log.insert(0, coord)
		self._attack_result_log.insert(0, result)

	def add_to_sunk_ships(self):
		self._sunk_ships += 1

	def get_sunk_ships(self):
		return self._sunk_ships

	def get_player_number(self):
		return self._player_number

	def get_attack_coord_log_value(self, element):
		return self._attack_coord_log[element][0], int(self._attack_coord_log[element][1:])
	
	def set_just_sunk_ship(self, value):
		self._just_sunk_ship = value

	def set_found_ship(self, value):
		self._found_ship = value