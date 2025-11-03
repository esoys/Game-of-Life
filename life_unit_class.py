import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, UNIT_WIDTH, UNIT_HEIGHT


class Life_Unit(pygame.sprite.Sprite):
    registry = []

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

        self.alive = False
        self.color = (60, 60, 60)

        self.image = pygame.Surface((UNIT_WIDTH, UNIT_HEIGHT))
        # self.image.fill("white")
        self.rect = self.image.get_rect(center=(self.__x, self.__y))

        self.__neighbours = []

        Life_Unit.registry.append(self)

    def change_alive_status(self):
        self.alive = not self.alive
        self.color = (60, 60, 60) if not self.alive else (200, 200, 200)

    def update(self):
        alive_counter = 0
        for neighbour in self.__neighbours:
            if neighbour.alive:
                alive_counter += 1

        if alive_counter == 3 and not self.alive:
            self.change_alive_status()

        if self.alive and (alive_counter == 1 or alive_counter >= 3):
            self.change_alive_status()

    def draw(self, screen):
        screen.fill(self.color, rect=self.rect)

    def get_neighbours(self):
        for other in Life_Unit.registry:
            if (
                (
                    other.__x == self.__x + self.__width
                    and (
                        other.__y == self.__y + self.__height
                        or other.__y == self.__y
                        or other.__y == self.__y - self.__height
                    )
                )
                or (
                    other.__x == self.__x
                    and (
                        other.__y == self.__y + self.__height
                        or other.__y == self.__y - self.__height
                    )
                )
                or (
                    other.__x == self.__x - self.__width
                    and (
                        other.__y == self.__y + self.__height
                        or other.__y == self.__y
                        or other.__y == self.__y - self.__height
                    )
                )
            ):
                self.__neighbours.append(other)
