from Island import Island
from Point import Point


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

    # check if only one point is in some edge

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

    def add_edge(self, edge):
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
            self.add_edge(edge)
            return True
        return False

    def is_double_edge(self, edge):
        return self.specific_edge_count(edge) == 2
