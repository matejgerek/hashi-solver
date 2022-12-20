from Game import Game
from ConsoleGUI import ConsoleGui
from DFS import DFS
from Backtracking import Backtracking
from ForwardChecking import ForwardChecking

# import json from games/game1.json
import json

print("Zadaj cislo levela(1-2): ", end="")
level = input()
game_data = json.JSONDecoder().decode(open("games/game" + level + ".json").read())
print()

game = Game(game_data['size'], game_data['islands'])
gui = ConsoleGui(game)
print("**************")
print("DFS")
print("**************")
dfs = DFS(game)
dfs.solve()
gui.draw_board()

print("**************")
print("Backtracking")
print("**************")
backtracking = Backtracking(game)
backtracking.solve()
gui.draw_board()

print("**************")
print("Forward Checking")
print("**************")
forward_checking = ForwardChecking(game)
forward_checking.solve()
gui.draw_board()
