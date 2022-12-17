class DFS:
    def __init__(self, game):
        self.game = game
        self.visited = set()

    def solve(self):
        self.game.reset()
        self.visited.clear()

        root = self.game.islands[0]
        i = 0
        graph = {}
        for island in self.game.islands:
            graph[island] = self.game.get_direct_neighbours(island)
            i = i + 1
        self.dfs(graph, root)

    def dfs(self, graph, root):
        if root not in self.visited:
            print("Visited island: ", end="")
            print(root)
            self.visited.add(root)
            neighbour_sorted = sorted(graph[root], key=lambda x: x.value, reverse=False)
            for neighbour in neighbour_sorted:
                if self.game.is_island_connection_viable(root, neighbour) or not self.visited.__contains__(neighbour):
                    self.game.connect_islands(root, neighbour)
                    print("Connect ", end="")
                    print(root, end="")
                    print(" to ", end="")
                    print(neighbour)
                else:
                    print(root, end="")
                    print(" cannot connect again with ", end="")
                    print(neighbour)
                self.dfs(graph, neighbour)
