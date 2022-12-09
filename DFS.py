from ConsoleGui import ConsoleGui
from Edge import Edge


class DFS:
    def __init__(self, game):
        self.game = game
        self.gui = ConsoleGui(game)

    def solve(self):
        self.gui.draw_board()
        self.dfs(self.game, self.game.get_islands()[0])
        if self.game.is_game_solved():
            print("Solved!")
        else:
            print("Not solved!")

    def dfs(self, game, starting_island):
        if self.game.is_solved():
            return True

        for island in game.get_unconnected_neighbours(starting_island):
            if self.game.add_edge_if_possible(Edge(starting_island, island)):
                self.gui.draw_board()
                if self.dfs(self.game, island):
                    return True
                self.gui.draw_board()
