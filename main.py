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
    dt = 100

    # create life units
    life_units = pygame.sprite.Group()
    Life_Unit.containers = life_units

    for x in range(0, (SCREEN_WIDTH // UNIT_WIDTH)):
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
                dt = 1 if start else 100 
                
                print("start = ", start)

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    for sprite in life_units:
                        sprite.on_click(event.pos)


        if start:
            for unit in Life_Unit.registry:
                Life_Unit.registry[unit].decide_next_state()

            for unit in Life_Unit.registry:
                Life_Unit.registry[unit].change_alive_status()
        

        screen.fill((0, 0, 0))
        life_units.update()
        life_units.draw(screen)
        pygame.display.flip()
        
        clock.tick(dt)
        
    
    pygame.quit()

if __name__ == "__main__":
    main()
