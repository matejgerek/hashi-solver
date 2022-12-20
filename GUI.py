import pygame

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
square_width = 50
square_height = 50
board_size = 8
size = width, height = board_size * square_width, board_size * square_height

wait = pygame.time.wait


def init_screen():
    screen = pygame.display.set_mode([500, 500])
    return screen


def draw_edge(screen, edge):
    x1 = square_width * edge.point1.x + 25
    y1 = square_height * edge.point1.y + 25
    x2 = square_width * edge.point2.x + 25
    y2 = square_height * edge.point2.y + 25
    if edge.is_horizontal():
        pygame.draw.line(screen, white, (x1, y1), (x2, y2), 5)
    else:
        pygame.draw.line(screen, white, (x1, y1), (x2, y2), 5)


def draw_double_edge(screen, edge):
    x1 = square_width * edge.point1.x + 25
    y1 = square_height * edge.point1.y + 25
    x2 = square_width * edge.point2.x + 25
    y2 = square_height * edge.point2.y + 25
    if edge.is_horizontal():
        pygame.draw.line(screen, white, (x1, y1 - 5), (x2, y2 - 5), 5)
        pygame.draw.line(screen, white, (x1, y1 + 5), (x2, y2 + 5), 5)
    else:
        pygame.draw.line(screen, white, (x1 - 5, y1), (x2 - 5, y2), 5)
        pygame.draw.line(screen, white, (x1 + 5, y1), (x2 + 5, y2), 5)


def draw_island(screen, island, is_current=False):
    island_width = square_width * island.x * 2 + 50
    island_height = square_height * island.y * 2 + 50
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
        self.screen = init_screen()

    def update(self, current_island):
        self.screen.fill(black)
        for edge in self.game.edges:
            if self.game.is_double_edge(edge):
                draw_double_edge(self.screen, edge)
            else:
                draw_edge(self.screen, edge)
        for island in self.game.islands:
            draw_island(self.screen, island, island.is_equal(current_island))
        pygame.display.flip()
        wait(300)

    def print_message(self, message):
        pygame.draw.rect(self.screen, white, (100, 100, 300, 300))
        font = pygame.font.Font(None, 36)
        text_render = font.render(message, 1, red)
        text_width, text_height = text_render.get_size()
        x = (500 - text_width) // 2
        y = (500 - text_height) // 2
        self.screen.blit(text_render, (x, y))
        pygame.display.flip()
        wait(1000)
