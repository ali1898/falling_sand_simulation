import pygame, sys
from grid import Grid

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
FPS = 120
GREY = (29, 29, 29)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand")

# Control the frame rate of the simulation
clock = pygame.time.Clock()
grid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

# Simulation Loop
while True:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Updating State
    # Drawing the grid
    window.fill(GREY)
    grid.draw(window)
    
    # Update Screen
    pygame.display.flip()
    clock.tick(FPS)