from constants import *
import pygame
import fluid_container
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

fluid_container = fluid_container.Fluid_container(50, 50)

fluid_container.change_level(-1)



set_point_slider = Slider(surface, 200, 50, 200, 20, min=0, max=99, step=1)
p_slider = Slider(surface, 200, 150, 200, 20, min=0, max=99, step=1)
i_slider = Slider(surface, 200, 250, 200, 20, min=0, max=99, step=1)
d_slider = Slider(surface, 200, 350, 200, 20, min=0, max=99, step=1)


set_point_output = TextBox(surface, 475, 35, 100, 50, fontSize=30)
p_output = TextBox(surface, 475, 135, 100, 50, fontSize=30)
i_output = TextBox(surface, 475, 235, 100, 50, fontSize=30)
d_output = TextBox(surface, 475, 335, 100, 50, fontSize=30)


def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False
        draw()
        update(events)
        pygame.display.update()

    pygame.quit()



def draw():
    surface.fill((255, 255, 255))#background
    fluid_container.draw(surface)
    # pygame.display.flip()



def update(events):
    fluid_container.update()
    set_point_output.setText(f"SP:{set_point_slider.getValue()}")
    p_output.setText(f"P:{p_slider.getValue()}")
    i_output.setText(f"I:{i_slider.getValue()}")
    d_output.setText(f"D:{d_slider.getValue()}")
    pygame_widgets.update(events)


if __name__ == "__main__":
    main()
