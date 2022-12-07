from Point import Point


class Island(Point):
    def __init__(self, x, y, value):
        super().__init__(x, y)
        self.value = value

    def __str__(self):
        return f"Island: {self.x}, {self.y}, {self.value}"

    def __repr__(self):
        return f"Island: {self.x}, {self.y}, {self.value}"

    def get_value(self):
        return self.value

    def is_vertical_neighbour(self, island):
        return self.x == island.x

    def is_horizontal_neighbour(self, island):
        return self.y == island.y

    def is_neighbour(self, island):
        return self.is_vertical_neighbour(island) \
               or self.is_horizontal_neighbour(island)
