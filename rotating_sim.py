import pygame
from constants import *
import math
class Rotating_sim():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 150
        self.height = 150
        self.start_angle = 0
        self.end_angle = 5
        self.circle_center = (self.x, self.y)
        self.angles = [0, 45, 90, 135, 180, 225, 270, 315]
        self.setpoint_angle = 0
        self.output_angle = 0

        self.acc = 0
        self.vel = 0
        self.drag = -0.5


    def update(self, clock):
        self.setpoint_angle = self.setpoint_angle % 360
        self.output_angle = self.output_angle % 360
        print(f"self.output_angle:{self.output_angle}")
        dt = clock.tick(60) / 1000.0
        self.output_angle += self.vel * (dt + 0.5) * (self.acc * dt**2)
        self.vel += self.acc * dt
        self.vel += self.drag


    def draw(self, surface):
        pygame.draw.circle(surface, RED, (self.x, self.y), self.width, width=0)

        font = pygame.font.Font(None, 36)  # Use default font, size 36


        for angle in self.angles:
        # Convert angle to radians
            radians = math.radians(angle)

            # Calculate position for the text
            text_x = self.circle_center[0] + int(self.width * math.cos(radians))
            text_y = self.circle_center[1] - int(self.width * math.sin(radians))  # Subtract because y-axis is inverted in Pygame

            # Render the text
            angle_text = font.render(f"{angle}°", True, BLACK)
            text_rect = angle_text.get_rect(center=(text_x, text_y))

            # Display the text
            surface.blit(angle_text, text_rect)
        # Draw setpoint line
        radians = math.radians(self.setpoint_angle)
        x = self.circle_center[0] + int(self.width * math.cos(radians))
        y = self.circle_center[1] - int(self.width * math.sin(radians))
        pygame.draw.line(surface, BLUE, self.circle_center, (x, y), width=4)

        # Draw output line
        radians = math.radians(self.output_angle)
        x = self.circle_center[0] + int(self.width * math.cos(radians))
        y = self.circle_center[1] - int(self.width * math.sin(radians))
        pygame.draw.line(surface, GREEN, self.circle_center, (x, y), width=4)



    def set_setpoint_angle(self, angle):
        self.setpoint_angle = angle


    def set_accelerate(self, speed):
        self.acc = speed
