from pygame.event import Event

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

    def handle_mouse_movement(self, event: Event):
        print(event)

    def handle_resize(self, event: Event):
        self._draw()