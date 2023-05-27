import random



letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

def get_random_coord():
	return (random.choice(letters) + random.choice(numbers))


def get_placement_coord2(coord1, ship):
	placement_line = random.choice(['row', 'column'])
	placement_direction = random.choice(['left_up', 'right_down'])
	if placement_line == 'row':
		if placement_direction == 'left_up':
			if int(coord1[1:]) - ship.get_ship_length() + 1 >= 1:
				coord2 = coord1[0] + str(int(coord1[1:]) - ship.get_ship_length() + 1)
			else:
				coord2 = coord1[0] + str(int(coord1[1:]) + ship.get_ship_length() - 1)
		if placement_direction == 'right_down':
			if int(coord1[1:]) + ship.get_ship_length() - 1 <= 10:
				coord2 = coord1[0] + str(int(coord1[1:]) + ship.get_ship_length() - 1)
			else:
				coord2 = coord1[0] + str(int(coord1[1:]) - ship.get_ship_length() + 1)
	if placement_line == 'column':
		if placement_direction == 'left_up':
			if letters.index(coord1[0]) - ship.get_ship_length() + 1 >= 0:
				coord2 = letters[letters.index(coord1[0]) - ship.get_ship_length() + 1] + coord1[1:]
			else:
				coord2 = letters[letters.index(coord1[0]) + ship.get_ship_length() - 1] + coord1[1:]
		if placement_direction == 'right_down':
			if letters.index(coord1[0]) + ship.get_ship_length() - 1 <= 9:
				coord2 = letters[letters.index(coord1[0]) + ship.get_ship_length() - 1] + coord1[1:]
			else:
				coord2 = letters[letters.index(coord1[0]) - ship.get_ship_length() + 1] + coord1[1:]
	return coord2


def check_placement_coord2_validity(coord1, coord2, player_board, ship):
	#Checks if there is already a ship at the coord entered
	if bool(player_board.get_coord_value_in_board(coord2)) == True:
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


def check_attack_coord_result(computer, attack_coord, enemy_board):
	if bool(enemy_board.get_coord_value_in_board(attack_coord)) == True:
		print(f"{attack_coord} is a hit!")
		computer.set_found_ship(True)
		return True
	print(f"{attack_coord} is a miss.")
	return False


def add_hit_to_ship_and_check_if_sunk(computer, attack_coord, enemy_ships, enemy_player):
	for ship in enemy_ships:
		for coord in ship.get_ship_location():
			if coord == attack_coord:
				ship.add_hit_to_ship(coord)
				if ship.check_if_sunk(enemy_player) == True:
					enemy_player.add_to_sunk_ships()
					computer.set_just_sunk_ship(True)
					computer.set_found_ship(False)


def get_attack_coord_after_one_hit(computer, computer_board, element):
		print("get_attack_coord_after_one_hit is called")
		last_hit_coord_letter, last_hit_coord_number = computer.get_attack_coord_log_value(element)
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
		if len(attack_coord_options) == 2 and bool(computer_board.get_coord_value_in_radar(attack_coord_options[0])) == True and bool(computer_board.get_coord_value_in_radar(attack_coord_options[1])) == True:
			return get_random_coord()
		if len(attack_coord_options) == 3 and bool(computer_board.get_coord_value_in_radar(attack_coord_options[0])) == True and bool(computer_board.get_coord_value_in_radar(attack_coord_options[1])) == True and bool(computer_board.get_coord_value_in_radar(attack_coord_options[2])) == True:
			return get_random_coord()
		if len(attack_coord_options) == 4 and bool(computer_board.get_coord_value_in_radar(attack_coord_options[0])) == True and bool(computer_board.get_coord_value_in_radar(attack_coord_options[1])) == True and bool(computer_board.get_coord_value_in_radar(attack_coord_options[2])) == True and bool(computer_board.get_coord_value_in_radar(attack_coord_options[3])) == True:
			return get_random_coord()
		#Randomly gets attack coord from attack coord options list
		return random.choice(attack_coord_options)