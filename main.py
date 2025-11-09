import pygame
from pygame.constants import K_BACKSPACE, MOUSEBUTTONDOWN
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

    for unit in Life_Unit.registry:
        Life_Unit.registry[unit].get_neighbours()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == 768:  # key down space, keyup: 769
                start = not start
                print("start = ", start)

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("maus", event.pos)
                    for sprite in life_units:
                        sprite.on_click(event.pos)
                    #pygame.display.flip()


        life_units.update()

        pygame.display.flip()

        clock.tick(10)

if __name__ == "__main__":
    main()
