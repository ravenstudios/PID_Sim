from constants import *
import time
import random
import pygame
import fluid_container
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

import ui
import PID_controller

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

fluid_container = fluid_container.Fluid_container(50, 50)


ui = ui.UI(surface)

sp, p, i, d = ui.get_values()


pid = PID_controller.PID_Controller(sp, p, i, d, -10000, 10000)

prev_time = time.time()

def reset():
    print("reset")
    sp, p, i, d = ui.get_values()


    pid = PID_controller.PID_Controller(sp, p, i, d, -100, 100)

def main():
    running = True

    RANDOM_SETPOINT = pygame.USEREVENT + 1
    pygame.time.set_timer(RANDOM_SETPOINT, 4000)

    while running:
        clock.tick(TICK_RATE)
        events = pygame.event.get()
        temp_value = 0
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    reset()
                if event.key == pygame.K_q:
                    running = False
            # if event.type == RANDOM_SETPOINT:  # Triggered every second
            #     if ui.set_point_slider.getValue() == 0:
            #         ui.set_point_slider.setValue(temp)
            #     else:
            #         temp = ui.set_point_slider.getValue()
            #         ui.set_point_slider.setValue(0)

        draw()
        update(events)
        pygame.display.update()

    pygame.quit()


# def update_time():
#     global prev_time
#     current_time = time.time()
#     dt = current_time - prev_time
#     prev_time = current_time
#     return dt

def draw():
    surface.fill((255, 255, 255))#background
    fluid_container.draw(surface)
    # pygame.display.flip()



def update(events):
    fluid_container.update(clock)
    ui.update(events)

    if ui.toggle_pid.getValue():
        sp, p, i, d = ui.get_values()
        pid.update_pid(sp, p, i, d)
        fluid_container.change_level(pid.calc(fluid_container.get_level(), clock.tick(60) / 1000.0))
    else:
        pid.reset()
        fluid_container.set_level(0)


if __name__ == "__main__":
    main()
