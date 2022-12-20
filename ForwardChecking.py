import sys
import time
import pygame


class ForwardChecking:
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
            self.forward_checking(graph, root, count, self.gui.update)
            count = count + 1
            if self.game.is_game_solved():
                print("Game is solved!")
                self.gui.print_message("Game is solved!")
                break
            else:
                print("Game is not solved!")
            if count == 8:
                break
        end_time = time.perf_counter()
        time_duration = (end_time - start_time) * 1000
        print("-------------------------------------------")
        if not self.game.is_game_solved():
            self.gui.print_message("Game is not solved!")
        print(f"Forward Checking works {time_duration:0.5f} milliseconds")
        print(f"Opened islands {self.island_count_visited} times ")
        print("-------------------------------------------")

    def forward_checking(self, graph, root, count, update):
        update(root)
        if root not in self.visited:
            self.visited.add(root)
            print(f"Visited root {root}")
            neighbours = {}
            for island in graph[root]:
                neighbours[island] = self.game.get_connected_neighbours(island).__len__()
            neighbours = dict(sorted(neighbours.items(), key=lambda item: item[1]))
            for neighbour in neighbours:
                print(f"Visited neighbour {neighbour}")
                self.island_count_visited = self.island_count_visited + 1
                if self.game.is_island_connection_viable(root, neighbour):
                    graph[neighbour] = self.game.get_direct_neighbours(neighbour, count)
                    self.game.connect_islands(root, neighbour)
                    if neighbour.value > 1:
                        self.forward_checking(graph, neighbour, count, update)
                else:
                    print("Returning back ...")
