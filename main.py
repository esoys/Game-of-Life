import pygame
from pygame.rect import RectType
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from life_unit_class import Life_Unit


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    # create life units
    life_units = []
    unit_width = 30
    unit_height = 30

    for y in range(0, (SCREEN_HEIGHT // unit_height)):
        life_units.append([])
        for x in range(0, SCREEN_WIDTH // unit_width):
            life_units[y].append(
                Life_Unit(
                    x * unit_width,
                    y * unit_height,
                    unit_width,
                    unit_height,
                )
            )

    print(life_units[0:1][:2])

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((50, 50, 50))

        for y in range(0, len(life_units)):
            for x in range(0, len(life_units[y])):
                pygame.draw.rect(screen, "white", life_units[y][x], width=1)

        # pygame.draw.rect(screen, "white", pygame.Rect(5, 5, 100, 100), width=1)
        # pygame.draw.rect(screen, "white", pygame.Rect(105, 105, 100, 100), width=1)
        # pygame.draw.rect(screen, "white", pygame.Rect(5, 105, 100, 100), width=1)
        # pygame.draw.rect(screen, "white", pygame.Rect(105, 5, 100, 100), width=1)
        pygame.display.flip()

        clock.tick(500)


if __name__ == "__main__":
    main()
