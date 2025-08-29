from pygame.event import Event

from dataclasses.moving_event import MovingEvent
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
        [offset, board_size] = self.view.get_board_details()
        pos = Coordinate.from_pixel(event.pos, offset, board_size)
        if(pos is None):
            return

        piece = self.model.get_cell(pos)
        if(piece is None):
            return
        
        self.model.start_piece_movement(MovingEvent(
            piece=piece,
            position=pos,
            valid_movements=piece.get_valid_movements(
                pos,
                self.model
            )
        ))
        self._draw()


    def handle_mouse_up(self, event: Event):
        movement = self.model.movement_piece
        if(movement is None):
            return

        [offset, board_size] = self.view.get_board_details()
        pos = Coordinate.from_pixel(event.pos, offset, board_size)
        if(pos is None or not movement.valid_move(pos)):
            self.model.end_piece_movement()
            self._draw()
            return

        self.model.move_piece(movement.position, pos)

        self.model.end_piece_movement()
        self._draw()
        

    def handle_mouse_movement(self, event: Event):
        if(self.model.movement_piece is None):
            return
        
        self._draw()

    def handle_resize(self, event: Event):
        self._draw()