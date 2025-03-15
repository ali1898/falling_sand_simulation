import pygame, sys
from grid import Grid
from particle import SandParticle
from particle import RockParticle

class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.cell_size = cell_size
        self.mode = "sand"

    def draw(self, window):
        self.grid.draw(window)

    def add_particle(self, row, column):
        if self.mode == "sand":
            particle = SandParticle
        elif self.mode == "rock":
            particle = RockParticle
            
        self.grid.add_particle(row, column, particle)
    
    def remove_particle(self, row, column):
        self.grid.remove_particle(row, column)
    
    def update(self):
        for row in range(self.grid.rows - 2, -1, -1):
            for column in range(self.grid.columns):
               particle = self.grid.get_cell(row, column) 
               if isinstance(particle, SandParticle):
                   new_pos = particle.update(self.grid, row, column)
                   if new_pos != (row, column):
                       self.grid.set_cell(new_pos[0], new_pos[1], particle)
                       self.grid.remove_particle(row, column)

    def restart(self):
        self.grid.clear()

    def handle_controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.handle_key(event)
        self.handle_mouse()
    
    def handle_key(self, event):
        if event.key == pygame.K_SPACE:
            self.restart()
        elif event.key == pygame.K_s:
            print("Sand Mode")
            self.mode = "sand"
        elif event.key == pygame.K_r:
            print("Rock Mode")
            self.mode = "rock"
        elif event.key == pygame.K_e:
            print("Eraser Mode")
            self.mode = "erase"
        elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    def handle_mouse(self):
        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            pos = pygame.mouse.get_pos()
            # Y coordinate
            row = pos[1] // self.cell_size
            # X coordinate
            column = pos[0] // self.cell_size
            self.add_particle(row, column)

