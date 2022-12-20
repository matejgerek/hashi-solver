import sys
import pygame
from Game import Game
from ForwardChecking import ForwardChecking
from GUI import GUI

# import json from games/game1.json
import json

print("Zadaj cislo levela(1-2): ", end="")
level = input()
game_data = json.JSONDecoder().decode(open("games/game" + level + ".json").read())
print()

pygame.init()
game = Game(game_data['size'], game_data['islands'])
gui = GUI(game)
dfs = ForwardChecking(game, gui)
dfs.solve()
sys.exit()
