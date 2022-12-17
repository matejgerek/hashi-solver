class DFS:
    def __init__(self, game):
        self.game = game
        self.visited = set()

    def solve(self):
        self.game.reset()
        self.visited.clear()

        root = self.game.islands[0]
        graph = {root: self.game.get_direct_neighbours(root)}
        self.dfs(graph, root)

    def dfs(self, graph, root):
        if root not in self.visited:
            print("======================================")
            print("Visited island: ", end="")
            print(root)
            self.visited.add(root)
            neighb = {}
            for island in graph[root]:
                neighb[island] = self.game.get_connected_neighbours(island).__len__()
            neighb = dict(sorted(neighb.items(), key=lambda item: item[1]))
            for neighbour in neighb:
                if self.game.is_island_connection_viable(root, neighbour):
                    graph[neighbour] = self.game.get_direct_neighbours(neighbour)
                    print("-- Connect ", end="")
                    print(root, end="")
                    print(" to ", end="")
                    print(neighbour)
                    self.game.connect_islands(root, neighbour)
                if neighbour.value > 1:
                    self.dfs(graph, neighbour)
