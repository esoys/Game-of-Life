import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

unit_width = SCREEN_WIDTH / 10
unit_height = SCREEN_HEIGHT / 10


class Life_Unit(pygame.Rect):
    color = "white"

    def __init__(self, top, left, width, height, alive=False):
        super().__init__(top, left, width, height)
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.alive = alive
