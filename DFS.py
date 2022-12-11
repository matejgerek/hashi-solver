from ConsoleGui import ConsoleGui
from Edge import Edge


class DFS:
    def __init__(self, game):
        self.game = game
        self.gui = ConsoleGui(game)

    def solve(self):
        # island = self.game.get_islands()[0]

        i = 0
        for island in self.game.get_islands():
            self.game.reset()
            print("DFS from " + str(island) + " iteration: " + str(i))
            i += 1
            print('Solving...')
            self.dfs(self.game, island)
            print('---')
            if self.game.is_game_solved():
                print("Solved!")
                self.gui.draw_board()
                return True
            else:
                print("Not solved!")
            self.gui.draw_board()

    def dfs(self, game, starting_island):
        if self.game.is_solved():
            return True
        neighbours = game.get_unconnected_neighbours(starting_island)
        for neighbour in neighbours:
            if self.game.connect_islands(starting_island, neighbour):
                # self.gui.draw_board()
                if self.dfs(game, neighbour):
                    return True
        return False
