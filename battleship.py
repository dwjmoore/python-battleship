class Battleship:
	def __init__(self):
		print("""
/////////////////////////////////////////////////////////////////////////////////

BBBBBB   AAAAA  TTTTTTT TTTTTTT L       EEEEEEE SSSSSSS H     H IIIIIII PPPPPP
B     B A     A    T       T    L       E       S       H     H    I    P     P
B     B A     A    T       T    L       E       S       H     H    I    P     P
BBBBBB  AAAAAAA    T       T    L       EEEEEE  SSSSSSS HHHHHHH    I    PPPPPP
B     B A     A    T       T    L       E             S H     H    I    P
B     B A     A    T       T    L       E             S H     H    I    P
BBBBBB  A     A    T       T    LLLLLLL EEEEEEE SSSSSSS H     H IIIIIII P

/////////////////////////////////////////////////////////////////////////////////

Select the number of players. Enter 1 or 2:
""")
		self.num_players = input("> ")
	