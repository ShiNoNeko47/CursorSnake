import pygame
import random

class Food:
    def __init__(self):
        self.x = random.randint(0, 790)
        self.y = random.randint(0, 590)
        self.color = (255, 255, 255)
        self.size = 10
    def eaten(self):
        self.x = random.randint(0, 790)
        self.y = random.randint(0, 590)
    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.size, self.size))


