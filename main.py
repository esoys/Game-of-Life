import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, UNIT_WIDTH, UNIT_HEIGHT
from life_unit_class import Life_Unit


def main():
    pygame.init()
    print("Starting Game \nof \nLife!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    print(type(screen))
    # create life units
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Life_Unit.containers = (updatable, drawable)

    for x in range(0, (SCREEN_WIDTH // UNIT_HEIGHT)):
        for y in range(0, SCREEN_HEIGHT // UNIT_HEIGHT):
            Life_Unit(x * UNIT_WIDTH, y * UNIT_HEIGHT, UNIT_WIDTH, UNIT_HEIGHT)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)

        for draw in drawable:
            draw.draw(screen)

        print("hallo", pygame.time.get_ticks)

        pygame.display.flip()
        dt = clock.tick(0.5) / 100000


if __name__ == "__main__":
    main()
