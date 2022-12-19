import sys

import pygame

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
square_width = 50
square_height = 50
board_size = 8
size = width, height = board_size * square_width, board_size * square_height


def draw_edge(screen, edge):
    offset = 20
    x1 = square_width * (edge.point1.x + 1)
    y1 = square_height * (edge.point1.y + 1)
    x2 = square_width * (edge.point2.x + 1)
    y2 = square_height * (edge.point2.y + 1)
    if edge.is_horizontal():
        pygame.draw.line(screen, white, (x1 + offset, y1), (x2 - offset, y2), 5)
    else:
        pygame.draw.line(screen, white, (x1, y1 + offset), (x2, y2 - offset), 5)


def draw_double_edge(screen, edge):
    offset = 20
    x1 = square_width * (edge.point1.x + 1)
    y1 = square_height * (edge.point1.y + 1)
    x2 = square_width * (edge.point2.x + 1)
    y2 = square_height * (edge.point2.y + 1)
    if edge.is_horizontal():
        pygame.draw.line(screen, white, (x1 + offset, y1 - 5), (x2 - offset, y2 - 5), 5)
        pygame.draw.line(screen, white, (x1 + offset, y1 + 5), (x2 - offset, y2 + 5), 5)
    else:
        pygame.draw.line(screen, white, (x1 - 5, y1 + offset), (x2 - 5, y2 - offset), 5)
        pygame.draw.line(screen, white, (x1 + 5, y1 + offset), (x2 + 5, y2 - offset), 5)


def draw_island(screen, island, is_current=False):
    island_width = square_width * (island.x + 1) * 2
    island_height = square_height * (island.y + 1) * 2
    pygame.draw.circle(screen, blue if is_current else white, (island_width // 2, island_height // 2), 20)
    font = pygame.font.Font(None, 36)
    text_render = font.render(str(island.get_value()), 1, red)
    text_width, text_height = text_render.get_size()
    x = (island_width - text_width) // 2
    y = (island_height - text_height) // 2
    screen.blit(text_render, (x, y))


class GUI:
    def __init__(self, game):
        self.game = game
        pygame.init()
        self.screen = pygame.display.set_mode(size)

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if self.game.is_solved():
                print("Solved!")
                sys.exit()
            self.screen.fill(black)
            for island in self.game.islands:
                draw_island(self.screen, island)
            for edge in self.game.edges:
                if self.game.is_double_edge(edge):
                    draw_double_edge(self.screen, edge)
                else:
                    draw_edge(self.screen, edge)
            pygame.display.flip()
