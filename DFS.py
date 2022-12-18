class DFS:
    def __init__(self, game):
        self.game = game
        self.visited = set()
        self.island_count_visited = 0

    def solve(self):
        count = 0
        while True:
            self.game.reset()
            self.visited.clear()

            root = self.game.islands[0]
            graph = {root: self.game.get_direct_neighbours(root, count)}
            self.dfs2(graph, root, count)
            count = count + 1
            if self.game.is_game_solved():
                print("Game is solved!")
                break
            else:
                print("Game is not solved!")
            if count == 8:
                break
        print(f"Opened islands {self.island_count_visited} times ")

    def dfs(self, graph, root, count):
        if root not in self.visited:
            print("======================================")
            self.visited.add(root)
            neighbours = {}
            for island in graph[root]:
                neighbours[island] = self.game.get_connected_neighbours(island).__len__()
            neighbours = dict(sorted(neighbours.items(), key=lambda item: item[1]))
            for neighbour in neighbours:
                print("Visited ", end="")
                print(root)
                self.island_count_visited = self.island_count_visited + 1
                if self.game.is_island_connection_viable(root, neighbour):
                    graph[neighbour] = self.game.get_direct_neighbours(neighbour, count)
                    print("-- Connect ", end="")
                    print(root, end="")
                    print(" to ", end="")
                    print(neighbour)
                    self.game.connect_islands(root, neighbour)
                    self.dfs(graph, neighbour, count)
                else:
                    print("Returning back ...")

    def dfs2(self, graph, root, count):
        if root not in self.visited:
            self.visited.add(root)
            print("Visited root ", end="")
            print(root)
            for neighbour in graph[root]:
                print("Visited neighbour ", end="")
                print(neighbour)
                graph[neighbour] = self.game.get_direct_neighbours(neighbour, count)
                self.island_count_visited = self.island_count_visited + 1
                if self.game.is_island_connection_viable(root, neighbour):
                    self.game.connect_islands(root, neighbour)
                    self.dfs(graph, neighbour, count)
                else:
                    print("Returning back ...")
