import sys
import time
import pygame


class DFS:
    def __init__(self, game, gui):
        self.game = game
        self.visited = set()
        self.island_count_visited = 0
        self.gui = gui

    def solve(self):
        start_time = time.perf_counter()
        count = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.game.reset()
            self.visited.clear()
            root = self.game.islands[0]
            graph = {root: self.game.get_direct_neighbours(root, count)}
            self.dfs(graph, root, count, self.gui.update)
            count = count + 1
            if self.game.is_game_solved():
                print("Game is solved!")
                break
            else:
                print("Game is not solved!")
            if count == 8:
                break
        pygame.quit()
        end_time = time.perf_counter()
        time_duration = (end_time - start_time) * 1000
        print("-------------------------------------------")
        print(f"DFS works {time_duration:0.5f} milliseconds")
        print(f"Opened islands {self.island_count_visited} times ")
        print("-------------------------------------------")

    def dfs(self, graph, root, count, update):
        update(root)
        if root not in self.visited:
            self.visited.add(root)
            print(f"Visited root {root}")
            for neighbour in graph[root]:
                print(f"Visited neighbour {neighbour}")
                graph[neighbour] = self.game.get_direct_neighbours(neighbour, count)
                self.island_count_visited = self.island_count_visited + 1
                if self.game.is_island_connection_viable(root, neighbour):
                    self.game.connect_islands(root, neighbour)
                    if graph[neighbour].__contains__(root):
                        graph[neighbour].remove(root)
                        graph[neighbour].append(root)
                    self.dfs(graph, neighbour, count, update)
