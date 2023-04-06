import player
import board


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
		while self.num_players != '1' and self.num_players != '2':
			self.num_players = input(
			 "Invalid entry. Please enter 1 for a one-player game or 2 for a two-player game: "
			)

	def one_player_game(self):
		print("This game mode still needs to be built.")

	def two_player_game(self):
		player1 = player.Player(1)
		player2 = player.Player(2)
		player1_board = board.Board()
		player2_board = board.Board()

		player1.place_ships(player1_board)
		player2.place_ships(player2_board)