class Board:

	def __init__(self):
		self._player_board = {}
		self._player_radar = {}

		for letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
			for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
				self._player_board[letter + num] = ''
				self._player_radar[letter + num] = ''

	def display_player_board(self):
		for key in self._player_board:
			globals()[f"{key}"] = self._player_board[key]
		print(f"""
	1	|	2	|	3	|	4	|	5	|	6	|	7	|	8	|	9	|	10
--------------------------------------------------------------------------------
A	{A1}	|	{A2}	|	{A3}	|	{A4}	|	{A5}	|	{A6}	|	{A7}	|	{A8}	|	{A9}	|	{A10}
--------------------------------------------------------------------------------
B	{B1}	|	{B2}	|	{B3}	|	{B4}	|	{B5}	|	{B6}	|	{B7}	|	{B8}	|	{B9}	|	{B10}
--------------------------------------------------------------------------------
C	{C1}	|	{C2}	|	{C3}	|	{C4}	|	{C5}	|	{C6}	|	{C7}	|	{C8}	|	{C9}	|	{C10}
--------------------------------------------------------------------------------
D	{D1}	|	{D2}	|	{D3}	|	{D4}	|	{D5}	|	{D6}	|	{D7}	|	{D8}	|	{D9}	|	{D10}
--------------------------------------------------------------------------------
E	{E1}	|	{E2}	|	{E3}	|	{E4}	|	{E5}	|	{E6}	|	{E7}	|	{E8}	|	{E9}	|	{E10}
--------------------------------------------------------------------------------
F	{F1}	|	{F2}	|	{F3}	|	{F4}	|	{F5}	|	{F6}	|	{F7}	|	{F8}	|	{F9}	|	{F10}
--------------------------------------------------------------------------------
G	{G1}	|	{G2}	|	{G3}	|	{G4}	|	{G5}	|	{G6}	|	{G7}	|	{G8}	|	{G9}	|	{G10}
--------------------------------------------------------------------------------
H	{H1}	|	{H2}	|	{H3}	|	{H4}	|	{H5}	|	{H6}	|	{H7}	|	{H8}	|	{H9}	|	{H10}
--------------------------------------------------------------------------------
I	{I1}	|	{I2}	|	{I3}	|	{I4}	|	{I5}	|	{I6}	|	{I7}	|	{I8}	|	{I9}	|	{I10}
--------------------------------------------------------------------------------
J	{J1}	|	{J2}	|	{J3}	|	{J4}	|	{J5}	|	{J6}	|	{J7}	|	{J8}	|	{J9}	|	{J10}
--------------------------------------------------------------------------------
""")

	def display_player_radar(self):
		for key in self._player_radar:
			globals()[f"{key}"] = self._player_radar[key]
		print(f"""
	1	|	2	|	3	|	4	|	5	|	6	|	7	|	8	|	9	|	10
--------------------------------------------------------------------------------
A	{A1}	|	{A2}	|	{A3}	|	{A4}	|	{A5}	|	{A6}	|	{A7}	|	{A8}	|	{A9}	|	{A10}
--------------------------------------------------------------------------------
B	{B1}	|	{B2}	|	{B3}	|	{B4}	|	{B5}	|	{B6}	|	{B7}	|	{B8}	|	{B9}	|	{B10}
--------------------------------------------------------------------------------
C	{C1}	|	{C2}	|	{C3}	|	{C4}	|	{C5}	|	{C6}	|	{C7}	|	{C8}	|	{C9}	|	{C10}
--------------------------------------------------------------------------------
D	{D1}	|	{D2}	|	{D3}	|	{D4}	|	{D5}	|	{D6}	|	{D7}	|	{D8}	|	{D9}	|	{D10}
--------------------------------------------------------------------------------
E	{E1}	|	{E2}	|	{E3}	|	{E4}	|	{E5}	|	{E6}	|	{E7}	|	{E8}	|	{E9}	|	{E10}
--------------------------------------------------------------------------------
F	{F1}	|	{F2}	|	{F3}	|	{F4}	|	{F5}	|	{F6}	|	{F7}	|	{F8}	|	{F9}	|	{F10}
--------------------------------------------------------------------------------
G	{G1}	|	{G2}	|	{G3}	|	{G4}	|	{G5}	|	{G6}	|	{G7}	|	{G8}	|	{G9}	|	{G10}
--------------------------------------------------------------------------------
H	{H1}	|	{H2}	|	{H3}	|	{H4}	|	{H5}	|	{H6}	|	{H7}	|	{H8}	|	{H9}	|	{H10}
--------------------------------------------------------------------------------
I	{I1}	|	{I2}	|	{I3}	|	{I4}	|	{I5}	|	{I6}	|	{I7}	|	{I8}	|	{I9}	|	{I10}
--------------------------------------------------------------------------------
J	{J1}	|	{J2}	|	{J3}	|	{J4}	|	{J5}	|	{J6}	|	{J7}	|	{J8}	|	{J9}	|	{J10}
--------------------------------------------------------------------------------
""")

	def insert_attack_result_into_board(self, attack_result, coord):
		if attack_result == True:
			self._player_board[coord] = 'X'
		else:
			self._player_board[coord] = 'O'
	
	def insert_attack_result_into_radar(self, attack_result, coord):
		if attack_result == True:
			self._player_radar[coord] = 'X'
		else:
			self._player_radar[coord] = 'O'

	def insert_placement_coords_into_board(self, coord1, coord2, ship):
		#Inputs ship symbols into coord1 and coord2
		self._player_board[coord1] = ship.get_ship_symbol()
		self._player_board[coord2] = ship.get_ship_symbol()
		#Inputs coord1 and coord2 into ship location array
		ship.append_placement_coord_to_ship_location(coord1)
		ship.append_placement_coord_to_ship_location(coord2)
		#Fills in the coordinates between coord1 and coord2 with ship symbols
		#and also inputs them into the ship location array
		if coord1[0] == coord2[0] and int(coord1[1:]) < int(coord2[1:]):
			for x in range(1, ship.get_ship_length() - 1):
				self._player_board[coord1[0] + str(int(coord1[1:]) + x)] = ship.get_ship_symbol()
				ship.append_placement_coord_to_ship_location(coord1[0] + str(int(coord1[1:]) + x))
		if coord1[0] == coord2[0] and int(coord1[1:]) > int(coord2[1:]):
			for x in range(1, ship.get_ship_length() - 1):
				self._player_board[coord2[0] + str(int(coord2[1:]) + x)] = ship.get_ship_symbol()
				ship.append_placement_coord_to_ship_location(coord2[0] + str(int(coord2[1:]) + x))
		if coord1[0] != coord2[0] and coord1[0] < coord2[0]:
			for x in range(1, ship.get_ship_length() - 1):
				self._player_board[chr(ord(coord1[0]) + x) + coord1[1:]] = ship.get_ship_symbol()
				ship.append_placement_coord_to_ship_location(chr(ord(coord1[0]) + x) + coord1[1:])
		if coord1[0] != coord2[0] and coord1[0] > coord2[0]:
			for x in range(1, ship.get_ship_length() - 1):
				self._player_board[chr(ord(coord2[0]) + x) + coord2[1:]] = ship.get_ship_symbol()
				ship.append_placement_coord_to_ship_location(chr(ord(coord2[0]) + x) + coord2[1:])

	def get_coord_value_in_radar(self, coord):
		return self._player_radar[coord]

	def get_coord_value_in_board(self, coord):
		return self._player_board[coord]