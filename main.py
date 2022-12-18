from Game import Game
from ConsoleGui import ConsoleGui
from DFS import DFS
import time

# import json from games/game1.json
import json

print("Zadaj cislo levela(1-2): ", end="")
level = input()
game_data = json.JSONDecoder().decode(open("games/game" + level + ".json").read())
print()

game = Game(game_data['size'], game_data['islands'])
gui = ConsoleGui(game)
start_time = time.perf_counter()
dfs = DFS(game)
end_time = time.perf_counter()
dfs.solve()
gui.draw_board()
time_duration = (end_time - start_time) * 1000
print(f"DFS works {time_duration:0.5f} milliseconds")
