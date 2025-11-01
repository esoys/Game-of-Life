import pygame


class Life_Unit(pygame.Rect):
    registry = []

    def __init__(self, top, left, width, height, alive=False):
        super().__init__(top, left, width, height)
        self.__top = top
        self.__left = left
        self.__width = width
        self.__height = height

        self.__neighbours = None

        self.alive = alive
        self.color = (60, 60, 60)
        Life_Unit.registry.append(self)

    def change_alive_status(self):
        self.alive = not self.alive
        self.color = (60, 60, 60) if not self.alive else (200, 200, 200)

    def update(self):
        alive_counter = 0
        for other in Life_Unit.registry:
            if (
                other.__top == (self.__top + self.__height)
                and (
                    other.__top == (self.__top - self.width)
                    or (other.__top == self.__top)
                    or (other.__top - self.width)
                )
                or (
                    other.__top == self.__top
                    and (
                        other.__left == self.left - self.width
                        or other.__left == self.left + self.__width
                    )
                    or (
                        other.__top == self.__top - self.__height
                        and (
                            other.__left == self.left - self.width
                            or other.__left == self.__left
                            or other.__left == self.left + self.__width
                        )
                    )
                )
            ) and other.alive:
                alive_counter += 1

            # (other.__top == self.__top and other.__left == self.__left - self.__width)
            # or (other.__top == self.__top and other.__left == self.__left + self.__width)
            # or (other.__top == self.__top - self.__width and other.__left == self.__left)
            # or (other.__top == self.__top + self.__width and other.__left == self.__left)
            #
        if alive_counter == 3 and not self.alive:
            self.change_alive_status()

        if self.alive and (alive_counter == 1 or alive_counter >= 3):
            self.change_alive_status()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self, width=1)
