import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.toggle import Toggle
import pygame

class UI():


    def __init__(self, surface):


        self.set_point_slider = Slider(surface, 200, 50, 200, 20, min=0, max=500, step=1, initial=50)
        self.p_slider = Slider(surface, 200, 150, 200, 20, min=0, max=100, step=0.01, initial=0)
        self.i_slider = Slider(surface, 200, 250, 200, 20, min=0, max=100, step=0.01, initial=0)
        self.d_slider = Slider(surface, 200, 350, 200, 20, min=0, max=100, step=0.01, initial=0)


        self.set_point_output = TextBox(surface, 475, 35, 100, 50, fontSize=30)
        self.p_output = TextBox(surface, 475, 135, 100, 50, fontSize=30)
        self.i_output = TextBox(surface, 475, 235, 100, 50, fontSize=30)
        self.d_output = TextBox(surface, 475, 335, 100, 50, fontSize=30)

        self.toggle_pid_output = TextBox(surface, 800, 50, 120, 40, fontSize=20)
        self.toggle_pid_output.setText("Toggle PID")
        self.toggle_pid = Toggle(surface, 730, 60, 25, 25)

    def update(self, events):
        self.set_point_output.setText(f"SP:{self.set_point_slider.getValue()}")
        self.p_output.setText(f"P:{self.p_slider.getValue()}")
        self.i_output.setText(f"I:{self.i_slider.getValue()}")
        self.d_output.setText(f"D:{self.d_slider.getValue()}")
        pygame_widgets.update(events)

    def get_values(self):
        return[
            self.set_point_slider.getValue(),
            self.p_slider.getValue(),
            self.i_slider.getValue(),
            self.d_slider.getValue()
        ]
