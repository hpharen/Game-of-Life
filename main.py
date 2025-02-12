import time
import pygame
import numpy as np

COLOUR_BACKGROUND = (10, 10, 10)
COLOUR_GRID = (40, 40, 40)
COLOUR_DIE_NEXT = (31, 199, 0)
COLOUR_ALIVE_NEXT = (57, 255, 20)

# with_progress flag = may want to update screen without going to next generation
def update(screen, cells, size, with_progress=False):
    #
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    # Takes shape of the field, cells.shape, iterates over each individual cell, row col
    for row, col in np.ndindex(cells.shape):
        # Take a cell, take top left cell and bottom right cell, everything in between, sum it up, not counting middle cell
        # Returns alive neighbours
        alive = np.sum(cells[row - 1 : row + 2, col - 1 : col + 2]) - cells[row, col]
        colour = COLOUR_BACKGROUND if cells[row, col] == 0 else COLOUR_ALIVE_NEXT

        # Game rules
        # If center cell is alive
        if cells[row, col] == 1:
            # If less than 2 alive neighbours, or more than 3 alive neighbours
            if alive < 2 or alive > 3:
                if with_progress:
                    colour = COLOUR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    colour = COLOUR_ALIVE_NEXT
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    colour = COLOUR_ALIVE_NEXT
    
        pygame.draw.rect(screen, colour, (col * size, row * size, size - 1, size - 1))

    return updated_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    cells = np.zeros((60, 80))  # 60 rows, 80 columns
    screen.fill(COLOUR_GRID)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // 10, pos[0] // 10

                # Ensure clicked position is within bounds
                if row < cells.shape[0] and col < cells.shape[1]:
                    cells[row, col] = 1
                    update(screen, cells, 10)
                    pygame.display.update()

        screen.fill(COLOUR_GRID)

        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()
        
        time.sleep(0.001)

if __name__ == '__main__':
    main()
