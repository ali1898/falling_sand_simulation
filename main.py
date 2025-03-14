import pygame, sys

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 120

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand")

# Control the frame rate of the simulation
clock = pygame.time.Clock()

# Simulation Loop
while True:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Updating State
    # Drawing the grid
    
    # Update Screen
    pygame.display.flip()
    clock.tick(FPS)