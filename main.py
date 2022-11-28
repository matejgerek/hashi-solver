from Game import Game
from ConsoleGui import ConsoleGui

# import json from games/game1.json
import json

game_data = json.JSONDecoder().decode(open("games/game1.json").read())

game = Game(game_data['size'], game_data['islands'])
gui = ConsoleGui(game)
gui.play()
