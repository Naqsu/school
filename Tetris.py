import pygame
import random

# Inicjalizacja pygame
pygame.init()

# Kolory
black = (0, 0, 0)
gray = (128, 128, 128)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
white = (255, 255, 255)

# Wymiary gry
width = 300
height = 600
block_size = 30

# Okno gry
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris")

# Czcionka do wyświetlania wyniku
font = pygame.font.Font(None, 36)

# Kształty tetrisa
shapes = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
]

# Kolory odpowiadające kształtom (bez czarnego)
shape_colors = [cyan, yellow, magenta, green, red, blue, white]

# Klasa klocka
class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

    def rotated_shape(self):
        return rotate_shape(self.shape, self.rotation)

# Funkcja obracająca kształt
def rotate_shape(shape, rotation):
    rotated = shape
    for _ in range(rotation % 4):  # Obrót o 90 stopni na każdą iterację
        rotated = [[rotated[y][x] for y in range(len(rotated))] for x in range(len(rotated[0]) - 1, -1, -1)]
    return rotated

# Funkcja do generowania siatki
def create_grid(locked_positions={}):
    grid = [[black for _ in range(width // block_size)] for _ in range(height // block_size)]
    for (x, y), color in locked_positions.items():
        grid[y][x] = color
    return grid

# Rysowanie siatki
def draw_grid(surface, grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            pygame.draw.rect(surface, grid[y][x], (x * block_size, y * block_size, block_size, block_size), 0)

    # Rysowanie linii siatki
    for i in range(len(grid)):
        pygame.draw.line(surface, gray, (0, i * block_size), (width, i * block_size))
    for j in range(len(grid[0])):
        pygame.draw.line(surface, gray, (j * block_size, 0), (j * block_size, height))

# Rysowanie kształtu na planszy
def draw_shape(surface, piece):
    shape = piece.rotated_shape()
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    surface,
                    piece.color,
                    (
                        (piece.x + x) * block_size,
                        (piece.y + y) * block_size,
                        block_size,
                        block_size,
                    ),
                    0,
                )

# Sprawdzanie kolizji
def valid_space(piece, grid):
    shape = piece.rotated_shape()
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid_x = piece.x + x
                grid_y = piece.y + y
                if grid_x < 0 or grid_x >= len(grid[0]) or grid_y >= len(grid):
                    return False
                if grid_y >= 0 and grid[grid_y][grid_x] != black:
                    return False
    return True

# Usuwanie pełnych linii i aktualizacja blokad
def clear_lines(locked):
    cleared = 0
    rows_to_check = list(set(y for (_, y) in locked))  # Wiersze do sprawdzenia
    rows_to_check.sort(reverse=True)  # Sprawdzanie od dołu

    for row in rows_to_check:
        if all((x, row) in locked for x in range(width // block_size)):  # Jeśli wiersz pełny
            cleared += 1
            # Usuwamy wszystkie bloki z tego wiersza
            for x in range(width // block_size):
                del locked[(x, row)]
            # Przesuwamy wszystkie bloki powyżej w dół
            for (x, y) in sorted(list(locked), key=lambda pos: pos[1], reverse=True):
                if y < row:
                    locked[(x, y + 1)] = locked.pop((x, y))

    return cleared

# Funkcja główna
def main():
    locked_positions = {}
    grid = create_grid(locked_positions)

    current_piece = Piece(3, 0, random.choice(shapes))
    next_piece = Piece(3, 0, random.choice(shapes))

    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 500
    score = 0

    running = True
    while running:
        grid = create_grid(locked_positions)
        screen.fill(black)

        # Aktualizacja czasu opadania
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid):
                current_piece.y -= 1
                for y, row in enumerate(current_piece.rotated_shape()):
                    for x, cell in enumerate(row):
                        if cell:
                            # Dodaj blok do zablokowanych pozycji
                            locked_positions[(current_piece.x + x, current_piece.y + y)] = current_piece.color
                #
