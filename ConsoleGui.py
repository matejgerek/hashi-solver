from Edge import Edge
from Point import Point


def print_space():
    print(" ", end="")


def print_island(island):
    print(island.get_value(), end="")


def print_edge(edge):
    if edge.is_horizontal():
        print("-", end="")
    elif edge.is_vertical():
        print("|", end="")


def get_point_from_input(message):
    print(message, " (x,y):")
    point = input()
    return Point(int(point[0]), int(point[2]))


def input_edge():
    source = get_point_from_input("Enter source point")
    destination = get_point_from_input("Enter destination point")
    edge = Edge(source, destination)
    return edge


class ConsoleGui:
    def __init__(self, game):
        self.game = game

    def draw_board(self):
        for y in range(self.game.get_size()):
            for x in range(self.game.get_size()):
                if self.game.is_island_at_position(x, y):
                    print_island(self.game.get_island_at_position(x, y))
                elif self.game.is_edge_at_position(x, y):
                    print_edge(self.game.get_edge_at_position(x, y))
                else:
                    print_space()
            print()
        print()

    def play(self):
        while True:
            self.draw_board()
            edge = input_edge()
            is_edge_added = self.game.add_edge_if_possible(edge)
            if not is_edge_added:
                print("Edge cannot be added")
            if self.game.is_game_solved():
                print("Game solved")
                break
