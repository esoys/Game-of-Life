import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, UNIT_WIDTH, UNIT_HEIGHT


class Life_Unit(pygame.sprite.Sprite):
    registry = {}


    def __init__(self, x_pos, y_pos, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

        self.alive = False
        self.next_alive = False
        self.color = (60, 60, 60)

        self.image = pygame.Surface((self.__width, self.__height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(
            left=self.__x_pos, top=self.__y_pos, width=self.__width, height=self.__height
        )

        self.__neighbours = []

        Life_Unit.registry[f"{self.__x}, {self.__y}"] = self


    def update(self):
        self.image.fill(self.color)


    def change_alive_status(self):
        self.alive = self.next_alive
        self.color = (60, 60, 60) if not self.alive else (200, 200, 200)


    def decide_next_state(self):
        alive_count = self.get_num_alive_neighbours()

        if not self.alive:
            self.next_alive = (alive_count == 3)
        else:
            self.next_alive = (alive_count == 2 or alive_count == 3)
                
   
    def get_num_alive_neighbours(self):
        alive_count = 0
        for neighbour in self.__neighbours:
            if neighbour.alive:
                alive_count += 1
        return alive_count

        
    def on_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.alive = not self.alive
            self.color = (60, 60, 60) if not self.alive else (200, 200, 200)
            self.next_alive = self.alive


    def get_neighbours(self):
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                elif f"{self.__x + x}, {self.__y + y}" in Life_Unit.registry:
                    self.__neighbours.append(Life_Unit.registry[f"{self.__x + x}, {self.__y + y}"])
                else:
                    continue
