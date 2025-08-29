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
        self.view.draw(
            self.model.itterate_board(),
            movement_piece=self.model.movement_piece
        )

    def handle_mouse_down(self, event: Event):
        try:
            [offset, board_size] = self.view.get_board_details()
            pos = Coordinate.from_pixel(event, offset, board_size)

            piece = self.model.get_cell(pos)
            if(piece is None):
                return
            
            self.model.start_piece_movement(pos)
            self._draw()

        except AssertionError:
            ...

    def handle_mouse_up(self, event: Event):
        movement = self.model.movement_piece
        if(movement is None):
            return

        [offset, board_size] = self.view.get_board_details()
        pos = Coordinate.from_pixel(event, offset, board_size)

        self.model.move_piece(movement.position, pos)

        self.model.end_piece_movement()
        self._draw()

    def handle_mouse_movement(self, event: Event):
        if(self.model.movement_piece is None):
            return
        
        self._draw()

    def handle_resize(self, event: Event):
        self._draw()