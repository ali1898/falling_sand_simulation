import pygame
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
    Simulation.handle_controls()
    
    # Updating State
    Simulation.update()

    # Drawing the grid
    window.fill(GREY)
    Simulation.draw(window)
    
    # Update Screen
    pygame.display.flip()
    clock.tick(FPS)