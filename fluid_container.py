import pygame
from constants import *
import random


class Fluid_container:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 500
        self.color = (255, 0, 0)
        self.fluid_level = 0
        self.change_rate = 0
        self.drain_rate = 0.5
        self.low_random, self.high_random = -1, 2

        self.acc = 0
        self.vel = 0
        self.drag = 0.5

        self.max_acc = 10000


    def update(self, clock):
        dt = clock.tick(60) / 1000.0
        self.fluid_level += self.vel * dt + 0.5 * self.acc * dt**2
        self.fluid_level = max(self.fluid_level, 0)
        self.fluid_level = min(self.fluid_level, self.height)
        self.vel += self.acc * dt



    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height), 0)
        y = self.y + self.height - self.fluid_level #draw from bottom up
        pygame.draw.rect(surface, (0, 0, 255), (self.x, y, self.width, self.fluid_level), 0)

        font = pygame.font.SysFont(None, 48)  # Default font and size 48
        text_obj = font.render(f"{self.fluid_level:2f}", True, (0, 0, 0))
        text_rect = text_obj.get_rect(center=(200, 500))
        surface.blit(text_obj, text_rect)

    def change_level(self, change_rate):
        self.acc = change_rate


    def get_level(self):
        return self.fluid_level



    def set_level(self, lvl):
        self.fluid_level = lvl
