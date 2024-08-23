from constants import *
import pygame
import fluid_container


clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

fluid_container = fluid_container.Fluid_container(50, 50)

fluid_container.change_level(-1)

def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background
    fluid_container.draw(surface)
    pygame.display.flip()



def update():
    fluid_container.update()



if __name__ == "__main__":
    main()
