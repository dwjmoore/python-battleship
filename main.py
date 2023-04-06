import battleship

game = battleship.Battleship()

if game.num_players == '1':
	game.one_player_game()
if game.num_players == '2':
	game.two_player_game()