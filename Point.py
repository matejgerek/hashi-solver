class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def get_position(self):
        return self.x, self.y

    def is_equal(self, other):
        return self.x == other.x and self.y == other.y

    def is_at_the_right(self, other):
        return self.x < other.x and self.y == other.y

    def is_at_the_left(self, other):
        return self.x > other.x and self.y == other.y

    def is_above(self, other):
        return self.x == other.x and self.y > other.y

    def is_below(self, other):
        return self.x == other.x and self.y < other.y
