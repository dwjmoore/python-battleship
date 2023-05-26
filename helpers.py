import random


def get_random_coord():
	letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
	numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
	return (random.choice(letters) + random.choice(numbers))


def check_placement_coord1_validity(coord1, player_board):
		if bool(player_board.get_coord_value_in_board(coord1)) == True:
			return False
		return True


def check_placement_coord2_validity(coord1, coord2, player_board, ship):
	if coord2 == coord1:
		return False
	#Checks if there is already a ship at the coord entered
	if bool(player_board.get_coord_value_in_board(coord2)) == True:
		return False
	#Checks if the ship is placed diagonally
	if coord1[0] != coord2[0] and coord1[1:] != coord2[1:]:
		return False
	#Check if the length between coords equals ship length
	if coord1[0] == coord2[0]:
		coords_length = abs(int(coord1[1:]) - int(coord2[1:])) + 1
	if coord1[0] != coord2[0]:
		coords_length = abs(ord(coord1[0]) - ord(coord2[0])) + 1
	if coords_length < ship.get_ship_length():
		return False
	if coords_length > ship.get_ship_length():
		return False
	#Check if there is a ship already between coord1 and coord2
	if coord1[0] == coord2[0] and int(coord1[1:]) < int(coord2[1:]):
		for x in range(1, ship.get_ship_length() - 1):
			if bool(player_board.get_coord_value_in_board(coord1[0] + str(int(coord1[1:]) + x))) == True:
				return False
	if coord1[0] == coord2[0] and int(coord1[1:]) > int(coord2[1:]):
		for x in range(1, ship.get_ship_length() - 1):
			if bool(player_board.get_coord_value_in_board(coord2[0] + str(int(coord2[1:]) + x))) == True:
				return False
	if coord1[0] != coord2[0] and coord1[0] < coord2[0]:
		for x in range(1, ship.get_ship_length() - 1):
			if bool(player_board.get_coord_value_in_board(chr(ord(coord1[0]) + x) + coord1[1:])) == True:
				return False
	if coord1[0] != coord2[0] and coord1[0] > coord2[0]:
		for x in range(1, ship.get_ship_length() - 1):
			if bool(player_board.get_coord_value_in_board(chr(ord(coord2[0]) + x) + coord2[1:])) == True:
				return False
	return True


def check_attack_coord_validity(coord, player_board):
	if player_board.get_coord_value_in_radar(coord) == 'X' or player_board.get_coord_value_in_radar(coord) == 'O':
		return False
	return True


def check_attack_coord_result(computer, attack_coord, enemy_board):
	if bool(enemy_board.get_coord_value_in_board(attack_coord)) == True:
		print(f"{attack_coord} is a hit!")
		computer.set_found_ship(True)
		return True
	print(f"{attack_coord} is a miss.")
	return False


def add_hit_to_ship_and_check_if_sunk(player, attack_coord, enemy_ships, enemy_player):
	for ship in enemy_ships:
		for coord in ship.get_ship_location():
			if coord == attack_coord:
				ship.add_hit_to_ship(coord)
				if ship.check_if_sunk(enemy_player) == True:
					enemy_player.add_to_sunk_ships()
					player.set_just_sunk_ship(True)
					player.set_found_ship(False)