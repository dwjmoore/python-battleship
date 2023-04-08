import player
import board
import ship


class Battleship:

	def __init__(self):
		print("""
///////////////////////////////////////////////////////////////////////////////

BBBBBB   AAAAA  TTTTTTT TTTTTTT L       EEEEEEE SSSSSSS H     H IIIIIII PPPPPP
B     B A     A    T       T    L       E       S       H     H    I    P     P
B     B A     A    T       T    L       E       S       H     H    I    P     P
BBBBBB  AAAAAAA    T       T    L       EEEEEE  SSSSSSS HHHHHHH    I    PPPPPP
B     B A     A    T       T    L       E             S H     H    I    P
B     B A     A    T       T    L       E             S H     H    I    P
BBBBBB  A     A    T       T    LLLLLLL EEEEEEE SSSSSSS H     H IIIIIII P

///////////////////////////////////////////////////////////////////////////////
""")
		self.num_players = input("Select the number of players. Enter 1 or 2: ")
		print()
		while self.num_players != '1' and self.num_players != '2':
			self.num_players = input(
			 "Invalid entry. Please enter 1 for a one-player game or 2 for a two-player game: "
			)
			print()

	def one_player_game(self):
		print("This game mode still needs to be built.")

	def two_player_game(self):
		player1 = player.Player(1)
		player2 = player.Player(2)
		board1 = board.Board()
		board2 = board.Board()
		carrier1 = ship.Ship('carrier')
		battleship1 = ship.Ship('battleship')
		cruiser1 = ship.Ship('cruiser')
		submarine1 = ship.Ship('submarine')
		destroyer1 = ship.Ship('destroyer')
		ships1 = [carrier1, battleship1, cruiser1, submarine1, destroyer1]
		carrier2 = ship.Ship('carrier')
		battleship2 = ship.Ship('battleship')
		cruiser2 = ship.Ship('cruiser')
		submarine2 = ship.Ship('submarine')
		destroyer2 = ship.Ship('destroyer')
		ships2 = [carrier2, battleship2, cruiser2, submarine2, destroyer2]

		player1.place_ships(board1, ships1)
		# input("Hit enter to begin ship placement for player two.")
		# print()
		# player2.place_ships(board2, ships2)