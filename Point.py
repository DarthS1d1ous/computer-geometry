import math
import pygame
import random


class Point:
    def __init__(self, x, y, vectorX=1, vectorY=1, v=2):
        self.x = x
        self.y = y
        self.v = v
        self.alpha = random.uniform(0, 2 * math.pi)
        # self.vector = [round(self.v * math.cos(self.alpha)), round(self.v * math.sin(self.alpha))]
        self.vector = [vectorX, vectorY]

    def draw(self, display, color, width=3):
        pygame.draw.circle(display, color, (self.x, self.y), width)

    def move1(self):
        self.vector = [round(self.v * math.cos(self.alpha)), round(self.v * math.sin(self.alpha))]
        self.x = self.x + self.vector[0]
        self.y = self.y + self.vector[1]

    def move2(self, size):
        if abs(self.x) > size[0]:
            self.vector[0] = 0
        if abs(self.y) > size[1]:
            self.vector[1] = 0
        self.x = self.x + self.vector[0]
        self.y = self.y + self.vector[1]
