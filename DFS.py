from ConsoleGui import ConsoleGui


class DFS:
    def __init__(self, game):
        self.game = game
        self.gui = ConsoleGui(game)

    def solve(self):
        self.game.reset()
        self.gui.draw_board()
        self.dfs(self.game)

    def dfs(self):
        if self.game.is_solved():
            return True

