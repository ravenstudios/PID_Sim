import pygame
from constants import *


class Fluid_container:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 200
        self.color = (255, 0, 0)
        self.fluid_level = 100
        self.change_rate = 0

    def update(self):
        if 0 < self.fluid_level < self.height :
            self.fluid_level += self.change_rate
        print(self.fluid_level)


    def draw(self, surface):
        bs = BLOCK_SIZE
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height), 0)
        y = self.y + self.height - self.fluid_level
        pygame.draw.rect(surface, (0, 0, 255), (self.x, y, self.width, self.fluid_level), 0)

    def change_level(self, lvl):
        self.change_rate = lvl
