import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, UNIT_WIDTH, UNIT_HEIGHT
from life_unit_class import Life_Unit


def main():
    pygame.init()
    print("Starting Game \nof \nLife!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    # create life units
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Life_Unit.containers = (updatable, drawable)

    for x in range(0, (SCREEN_WIDTH // UNIT_HEIGHT)):
        for y in range(0, SCREEN_HEIGHT // UNIT_HEIGHT):
            new_unit = Life_Unit(
                x * UNIT_WIDTH, y * UNIT_HEIGHT, UNIT_WIDTH, UNIT_HEIGHT
            )
            updatable.add(new_unit)
            drawable.add(new_unit)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((60, 60, 60))

        updatable.update()

        drawable.draw(screen)
        print("draw")

        pygame.display.flip()
        clock.tick(1)


if __name__ == "__main__":
    main()
