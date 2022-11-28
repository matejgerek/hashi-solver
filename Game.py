# hashiwokakero game
import random


class Game:
    def __init__(self, size):
        self.size = size
        self.board = [[0 for x in range(size)] for y in range(size)]

    def __str__(self):
        return str(self.board)

    def __repr__(self):
        return str(self.board)

    def add_bridge(self, x, y):
        self.board[x][y] += 1

    def remove_bridge(self, x, y):
        self.board[x][y] -= 1

    def get_bridge(self, x, y):
        return self.board[x][y]

    def get_size(self):
        return self.size

    def get_board(self):
        return self.board

    # Add public method generate_random_board here
    def generate_random_board(self):
        for x in range(self.size):
            for y in range(self.size):
                self.board[x][y] = random.randint(0, 4)
