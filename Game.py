from Island import Island
from Point import Point
from Edge import Edge


class Game:
    def __init__(self, size, islands):
        self.islands = []
        self.edges = []
        self.size = size
        for island in islands:
            self.add_island(Island(island['x'], island['y'], island['value']))

    def __str__(self):
        return str(self.islands) + str(self.edges)

    def __repr__(self):
        return str(self.islands) + str(self.edges)

    def add_island(self, island):
        self.islands.append(island)

    def get_islands(self):
        return self.islands

    def get_size(self):
        return self.size

    def get_edges(self):
        return self.edges

    def get_islands_positions(self):
        return [Point(island.x, island.y) for island in self.get_islands()]

    def is_edge_between_islands(self, edge):
        return edge.point1 in self.get_islands_positions() \
               and edge.point2 in self.get_islands_positions()

    def get_vertical_edges(self):
        vertical_edges = []
        for edge in self.edges:
            if edge.is_vertical():
                vertical_edges.append(edge)
        return vertical_edges

    def get_horizontal_edges(self):
        horizontal_edges = []
        for edge in self.edges:
            if edge.is_horizontal():
                horizontal_edges.append(edge)
        return horizontal_edges

    def is_edge_interfering_with_edge(self, edge):
        if edge.is_horizontal():
            for vertical_edge in self.get_vertical_edges():
                if vertical_edge.point1.x == edge.point1.x and \
                        vertical_edge.point1.y < edge.point1.y < vertical_edge.point2.y:
                    return True
        elif edge.is_vertical():
            for horizontal_edge in self.get_horizontal_edges():
                if horizontal_edge.point1.y == edge.point1.y and \
                        horizontal_edge.point1.x < edge.point1.x < horizontal_edge.point2.x:
                    return True
        return False

    def __get_islands_between(self, edge):
        islands = []
        for island in self.islands:
            if Point(island.x, island.y) in edge.get_points_between():
                islands.append(island)
        return islands

    def is_edge_between_more_than_two_islands(self, edge):
        return len(self.__get_islands_between(edge)) > 2

    def is_island_at_position(self, x, y):
        for island in self.islands:
            if island.get_position() == Point(x, y).get_position():
                return True
        return False

    def get_island_at_position(self, x, y):
        for island in self.islands:
            if island.get_position() == Point(x, y).get_position():
                return island
        return None

    def is_edge_at_position(self, x, y):
        for edge in self.edges:
            if Point(x, y) in edge.get_points_between():
                return True
        return False

    def get_edge_at_position(self, x, y):
        for edge in self.edges:
            if Point(x, y) in edge.get_points_between():
                return edge
        return None

    def __add_edge(self, edge):
        self.edges.append(edge)

    def remove_edge(self, edge):
        self.edges.remove(edge)

    def get_island_edges(self, island):
        island_edges = []
        point = Point(island.x, island.y)
        for edge in self.edges:
            edge_points = edge.get_points()
            if point in edge_points:
                island_edges.append(edge)

        return island_edges

    def is_game_solved(self):
        for island in self.islands:
            if island.get_value() != len(self.get_island_edges(island)):
                return False
        return True

    def specific_edge_count(self, edge):
        count = 0
        for e in self.edges:
            if e.point1 == edge.point1 and e.point2 == edge.point2 or \
                    e.point1 == edge.point2 and e.point2 == edge.point1:
                count += 1
        return count

    def add_edge_if_possible(self, edge):
        if self.is_edge_between_islands(edge) \
                and not self.is_edge_interfering_with_edge(edge) \
                and not self.is_edge_between_more_than_two_islands(edge) \
                and self.specific_edge_count(edge) < 2:
            self.__add_edge(edge)
            return True
        return False

    def connect_islands(self, island1, island2):
        self.add_edge_if_possible(Edge(island1, island2))

    def is_double_edge(self, edge):
        return self.specific_edge_count(edge) == 2

    def get_neighbours(self, island):
        neighbours = []
        for otherIsland in self.get_islands():
            if island != otherIsland and island.is_neighbour(otherIsland):
                neighbours.append(otherIsland)
        return neighbours

    def get_island_edges(self, island):
        edges = []
        for edge in self.get_edges():
            if edge.is_connected_to_island(island):
                edges.append(edge)
        return edges

    def get_connected_neighbours(self, island):
        neighbours = []
        for edge in self.get_island_edges(island):
            neighbours.append(edge.get_other_island(island))
        return neighbours

    def is_island_connection_viable(self, island1, island2):
        return island1.is_neighbour(island2) and len(
            self.get_connected_neighbours(island1)) < island1.get_value() and len(
            self.get_connected_neighbours(island2)) < island2.get_value()

    def get_unconnected_neighbours(self, island):
        neighbours = []
        for neighbour in self.get_neighbours(island):
            if self.is_island_connection_viable(island, neighbour):
                neighbours.append(neighbour)
        return neighbours

    def is_solved(self):
        for island in self.get_islands():
            if island.get_value() != len(self.get_connected_neighbours(island)):
                return False
        return True

    def get_direct_neighbours(self, island):
        direct_neighbours = []
        neighbours = self.get_neighbours(island)
        column = island.get_position()[0]
        row = island.get_position()[1]
        # up
        while row > 0:
            row = row - 1
            for neighbour in neighbours:
                if Point(column, row) == Point(neighbour.x, neighbour.y):
                    direct_neighbours.append(neighbour)
                    row = 0
        # down
        column = island.get_position()[0]
        row = island.get_position()[1]
        while row < self.size:
            row = row + 1
            for neighbour in neighbours:
                if Point(column, row) == Point(neighbour.x, neighbour.y):
                    direct_neighbours.append(neighbour)
                    row = self.size
        # left
        column = island.get_position()[0]
        row = island.get_position()[1]
        while column > 0:
            column = column - 1
            for neighbour in neighbours:
                if Point(column, row) == Point(neighbour.x, neighbour.y):
                    direct_neighbours.append(neighbour)
                    column = 0
        # right
        column = island.get_position()[0]
        row = island.get_position()[1]
        while column < self.size:
            column = column + 1
            for neighbour in neighbours:
                if Point(column, row) == Point(neighbour.x, neighbour.y):
                    direct_neighbours.append(neighbour)
                    column = self.size
        return direct_neighbours

    def reset(self):
        self.edges = []
