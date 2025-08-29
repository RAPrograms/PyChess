from pygame.event import Event

from dataclasses.units import Coordinate
from mvc.model import Model
from mvc.view import View

class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

        view.set_controller(self)
        self._draw()

    def _draw(self):
        self.view.draw(self.model.itterate_board())

    def handle_mouse_down(self, event: Event):
        try:
            [offset, board_size] = self.view.get_board_details()
            Coordinate.from_pixel(event, offset, board_size)
        except AssertionError:
            ...

    def handle_mouse_up(self, event: Event):
        ...

    def handle_mouse_movement(self, event: Event):
        ...

    def handle_resize(self, event: Event):
        self._draw()