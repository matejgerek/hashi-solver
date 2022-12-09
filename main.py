from Game import Game
from ConsoleGui import ConsoleGui

# import json from games/game1.json
import json

game_data = json.JSONDecoder().decode(open("games/game1.json").read())

game = Game(game_data['size'], game_data['islands'])
gui = ConsoleGui(game)
gui.draw_board()
island1 = game.get_island_at_position(0, 0)
island2 = game.get_island_at_position(3, 0)
game.connect_islands(island1, island2)
gui.draw_board()
print('connected neighbours', game.get_connected_neighbours(island1))
print('unconnected neighbours', game.get_unconnected_neighbours(island1))
