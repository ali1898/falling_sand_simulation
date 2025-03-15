import pygame

class Grid:
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, window):
        for row in range(self.rows):
            for column in range(self.columns):
                # Get the particle of the current cell
                particle = self.cells[row][column]
                if particle is not None:
                    color = particle.color
                    pygame.draw.rect(window, color,
                                 (column * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))
    
    def add_particle(self, row, column, particle_type):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.cells[row][column] = particle_type()
    
    def remove_particle(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.cells[row][column] = None
    
    def is_cell_empty(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            if self.cells[row][column] is None:
                return True
            return False
    
    def set_cell(self, row, column, particle):
        if not(0 <= row < self.rows and 0 <= column < self.columns):
            return
        self.cells[row][column] = particle
    
    def get_cell(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return self.cells[row][column]
        return None