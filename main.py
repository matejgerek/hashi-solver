from Game import Game
from ConsoleGui import ConsoleGui

# import json from games/game1.json
import json

print("Zadaj cislo levela(1-2): ", end="")
level = input()
game_data = json.JSONDecoder().decode(open("games/game" + level + ".json").read())

game = Game(game_data['size'], game_data['islands'])
gui = ConsoleGui(game)
gui.play()
