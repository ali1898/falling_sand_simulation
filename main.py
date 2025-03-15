import pygame, sys
from simulation import Simulation


pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 5
FPS = 120
GREY = (29, 29, 29)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand")

# Control the frame rate of the simulation
clock = pygame.time.Clock()
Simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

# Simulation Loop
while True:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Simulation.restart()

    # Get mouse button pressed on each frame
    buttons = pygame.mouse.get_pressed()
    if buttons[0]:
        pos = pygame.mouse.get_pos()
        # Y coordinate
        row = pos[1] // CELL_SIZE
        # X coordinate
        column = pos[0] // CELL_SIZE
        Simulation.add_particle(row, column)

    # Updating State
    Simulation.update()

    # Drawing the grid
    window.fill(GREY)
    Simulation.draw(window)
    
    # Update Screen
    pygame.display.flip()
    clock.tick(FPS)