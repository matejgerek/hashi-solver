import math
from Point import Point


class Edge:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.length = self.get_length()
        if self.length == 0:
            raise Exception("Edge length is 0")
        if not self.is_horizontal() and not self.is_vertical():
            raise Exception("Edge is not horizontal or vertical")

    def get_length(self):
        return math.sqrt((self.point1.x - self.point2.x) ** 2 + (self.point1.y - self.point2.y) ** 2)

    def __str__(self):
        return "Edge: " + str(self.point1) + " " + str(self.point2)

    def __repr__(self):
        return "Edge: " + str(self.point1) + " " + str(self.point2)

    def is_equal(self, other):
        return (self.point1 == other.point1 and self.point2 == other.point2) or (
                self.point1 == other.point2 and self.point2 == other.point1)

    # check if edge is horizontal or vertical
    def is_horizontal(self):
        return self.point1.y == self.point2.y

    def is_vertical(self):
        return self.point1.x == self.point2.x

    def get_points_between(self):
        points = []
        if self.is_horizontal():
            for x in range(min(self.point1.x, self.point2.x) + 1, max(self.point1.x, self.point2.x)):
                points.append(Point(x, self.point1.y))
        elif self.is_vertical():
            for y in range(min(self.point1.y, self.point2.y) + 1, max(self.point1.y, self.point2.y)):
                points.append(Point(self.point1.x, y))
        return points

    def get_points(self):
        return [self.point1] + self.get_points_between() + [self.point2]
