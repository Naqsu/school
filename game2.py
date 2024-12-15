import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 1000
GRID_SIZE = 10
CELL_SIZE = 40
MARGIN = 5
GRID_WIDTH = GRID_SIZE * (CELL_SIZE + MARGIN) - MARGIN
GRID_HEIGHT = GRID_SIZE * (CELL_SIZE + MARGIN) - MARGIN
GRID_START_X = (SCREEN_WIDTH - GRID_WIDTH) // 2
GRID_START_Y = (SCREEN_HEIGHT - GRID_HEIGHT) // 2

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Blast!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 100, 255)
RED = (255, 100, 100)
TRANSPARENT_GREEN = (100, 255, 100, 128)

FONT = pygame.font.Font(None, 36)
GRID = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

BLOCK_SHAPES = [
    [[1]], 
    [[1, 1]], 
    [[1], [1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1]],
    [[1], [1], [1]],
    [[1, 1, 1], [0, 1, 0]],
]

def draw_grid():
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = WHITE if GRID[y][x] == 0 else BLUE
            pygame.draw.rect(
                SCREEN,
                color,
                (
                    GRID_START_X + x * (CELL_SIZE + MARGIN),
                    GRID_START_Y + y * (CELL_SIZE + MARGIN),
                    CELL_SIZE,
                    CELL_SIZE,
                ),
            )

def can_place_block(block, x, y):
    for by, row in enumerate(block):
        for bx, cell in enumerate(row):
            if cell and (
                x + bx >= GRID_SIZE or
                y + by >= GRID_SIZE or
                GRID[y + by][x + bx] != 0
            ):
                return False
    return True

def place_block(block, x, y):
    for by, row in enumerate(block):
        for bx, cell in enumerate(row):
            if cell:
                GRID[y + by][x + bx] = 1

def clear_full_lines():
    global GRID
    GRID = [row for row in GRID if not all(row)]
    cleared = GRID_SIZE - len(GRID)
    GRID = [[0] * GRID_SIZE for _ in range(cleared)] + GRID
    return cleared

def generate_blocks():
    return [random.choice(BLOCK_SHAPES) for _ in range(3)]

def draw_blocks(blocks, selected_block=None, mouse_pos=None, highlight_pos=None):
    for i, block in enumerate(blocks):
        if selected_block == block:
            continue
        draw_single_block(
            block,
            SCREEN_WIDTH // 2 - 100 + i * 150,
            SCREEN_HEIGHT - 200,
            RED,
        )
    if selected_block and mouse_pos:
        draw_single_block(
            selected_block,
            mouse_pos[0],
            mouse_pos[1],
            RED,
            offset_center=True,
        )
    if selected_block and highlight_pos:
        hx, hy = highlight_pos
        draw_single_block(
            selected_block,
            GRID_START_X + hx * (CELL_SIZE + MARGIN),
            GRID_START_Y + hy * (CELL_SIZE + MARGIN),
            TRANSPARENT_GREEN,
        )

def draw_single_block(block, x, y, color, offset_center=False):
    block_width = len(block[0]) * (CELL_SIZE + MARGIN)
    block_height = len(block) * (CELL_SIZE + MARGIN)
    if offset_center:
        x -= block_width // 2
        y -= block_height // 2
    for by, row in enumerate(block):
        for bx, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    SCREEN,
                    color,
                    (
                        x + bx * (CELL_SIZE + MARGIN),
                        y + by * (CELL_SIZE + MARGIN),
                        CELL_SIZE,
                        CELL_SIZE,
                    ),
                )

def get_grid_position(mouse_pos):
    mx, my = mouse_pos
    x = (mx - GRID_START_X) // (CELL_SIZE + MARGIN)
    y = (my - GRID_START_Y) // (CELL_SIZE + MARGIN)
    return (x, y) if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE else None

def is_game_over(blocks):
    for block in blocks:
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if can_place_block(block, x, y):
                    return False
    return True

def main_menu():
    running = True
    while running:
        SCREEN.fill(BLACK)
        title_text = FONT.render("BLOCK BLAST!", True, WHITE)
        SCREEN.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 200))
        start_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, 400, 200, 50)
        exit_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, 500, 200, 50)
        pygame.draw.rect(SCREEN, GRAY, start_button)
        pygame.draw.rect(SCREEN, GRAY, exit_button)
        start_text = FONT.render("Start", True, BLACK)
        exit_text = FONT.render("Exit", True, BLACK)
        SCREEN.blit(start_text, (start_button.x + start_button.width // 2 - start_text.get_width() // 2, start_button.y + 10))
        SCREEN.blit(exit_text, (exit_button.x + exit_button.width // 2 - exit_text.get_width() // 2, exit_button.y + 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if start_button.collidepoint(mx, my):
                    running = False
                elif exit_button.collidepoint(mx, my):
                    pygame.quit()
                    sys.exit()
        pygame.display.flip()

def main():
    main_menu()
    clock = pygame.time.Clock()
    blocks = generate_blocks()
    selected_block = None
    dragging = False
    mouse_pos = None
    score = 0
    running = True
    while running:
        SCREEN.fill(BLACK)
        draw_grid()
        highlight_pos = None
        if selected_block and mouse_pos:
            grid_pos = get_grid_position(mouse_pos)
            if grid_pos and can_place_block(selected_block, grid_pos[0], grid_pos[1]):
                highlight_pos = grid_pos
        draw_blocks(blocks, selected_block, mouse_pos, highlight_pos)
        score_text = FONT.render(f"Score: {score}", True, WHITE)
        SCREEN.blit(score_text, (10, 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for i, block in enumerate(blocks):
                    block_width = len(block[0]) * (CELL_SIZE + MARGIN)
                    block_height = len(block) * (CELL_SIZE + MARGIN)
                    block_x = SCREEN_WIDTH // 2 - 100 + i * 150
                    block_y = SCREEN_HEIGHT - 200
                    if block_x <= mx <= block_x + block_width and block_y <= my <= block_y + block_height:
                        selected_block = block
                        dragging = True
                        break
            elif event.type == pygame.MOUSEBUTTONUP and dragging:
                dragging = False
                if selected_block and highlight_pos:
                    place_block(selected_block, highlight_pos[0], highlight_pos[1])
                    blocks.remove(selected_block)
                    if not blocks:
                        blocks = generate_blocks()
                    score += clear_full_lines()
                selected_block = None
                mouse_pos = None
            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
        if is_game_over(blocks):
            game_over_text = FONT.render("GAME OVER", True, RED)
            SCREEN.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
        pygame.display.flip()
        clock.tick(240)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
