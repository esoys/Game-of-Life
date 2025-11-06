import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, UNIT_WIDTH, UNIT_HEIGHT
from life_unit_class import Life_Unit


def main():
    pygame.init()
    print("Starting Game \nof \nLife!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    start = False

    # create life units
    life_units = pygame.sprite.Group()
    Life_Unit.containers = life_units

    for x in range(0, (SCREEN_WIDTH // UNIT_HEIGHT)):
        for y in range(0, SCREEN_HEIGHT // UNIT_HEIGHT):
            new_unit = Life_Unit(
                x * UNIT_WIDTH, y * UNIT_HEIGHT, UNIT_WIDTH, UNIT_HEIGHT
            )
            life_units.add(new_unit)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        life_units.draw(screen)
        while start:
            print("tick")
            clock.tick(1)

        life_units.update()
        pygame.display.flip()


if __name__ == "__main__":
    main()
