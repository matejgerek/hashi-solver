# import Game from game
from Game import Game

game = Game(7)
game.generate_random_board()
print(game.get_board())
