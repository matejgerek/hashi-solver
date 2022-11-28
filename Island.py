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
