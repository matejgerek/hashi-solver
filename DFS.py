import time
class DFS:
    def __init__(self, game):
        self.game = game
        self.visited = set()
        self.island_count_visited = 0

    def solve(self):
        start_time = time.perf_counter()
        count = 0
        while True:
            self.game.reset()
            self.visited.clear()

            root = self.game.islands[0]
            graph = {root: self.game.get_direct_neighbours(root, count)}
            self.dfs(graph, root, count)
            count = count + 1
            if self.game.is_game_solved():
                print("Game is solved!")
                break
            else:
                print("Game is not solved!")
            if count == 8:
                break
        end_time = time.perf_counter()
        time_duration = (end_time - start_time) * 1000
        print("-------------------------------------------")
        print(f"DFS works {time_duration:0.5f} milliseconds")
        print(f"Opened islands {self.island_count_visited} times ")
        print("-------------------------------------------")

    def dfs(self, graph, root, count):
        if root not in self.visited:
            self.visited.add(root)
            print(f"Visited root {root}")
            neighbours = {}
            for island in graph[root]:
                neighbours[island] = self.game.get_connected_neighbours(island).__len__()
            neighbours = dict(sorted(neighbours.items(), key=lambda item: item[1]))
            for neighbour in neighbours:
                print(f"Visited neighbour {root}")
                self.island_count_visited = self.island_count_visited + 1
                if self.game.is_island_connection_viable(root, neighbour):
                    graph[neighbour] = self.game.get_direct_neighbours(neighbour, count)
                    self.game.connect_islands(root, neighbour)
                    self.dfs(graph, neighbour, count)
                else:
                    print("Returning back ...")
