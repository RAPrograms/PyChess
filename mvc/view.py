from pygame import locals, draw, mouse
from typing import Any, Generator

from dataclasses.moving_event import MovingEvent
from dataclasses.units import Coordinate
from dataclasses.window import Window

from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.king import King

cWhite = (255, 255, 255)
cBlack = (0,255,0)

class View:
    def __init__(self, window: Window):
        self.window = window


    def set_controller(self, instance):
        self.window.add_event(locals.MOUSEBUTTONDOWN, instance.handle_mouse_down)
        self.window.add_event(locals.MOUSEBUTTONUP, instance.handle_mouse_up)
        self.window.add_event(locals.MOUSEMOTION, instance.handle_mouse_movement)
        self.window.add_event(locals.VIDEORESIZE, instance.handle_resize)

    def get_board_details(self):
        board_size = self.window.smallest_boundary
        half_board = board_size / 2
        
        offset = self.window.screen_center
        offset[0] -= half_board
        offset[1] -= half_board

        return [offset, board_size]
    
    def draw(
        self,
        data: Generator[tuple[Coordinate, None | Rook | Knight | Bishop | King | Queen | Bishop | Knight | Rook | Pawn], Any, None],
        movement_piece: MovingEvent | None = None
    ):
        self.window.surface.fill((0,0,0))

        [offset, board_size] = self.get_board_details()
        cell_size = board_size / 8

        for pos, value in data:
            col, row = pos.position
            colour = cWhite if (pos.index + (row % 2)) % 2 == 0 else cBlack

            draw.rect(self.window.surface, colour, (
                offset[0] + (col * cell_size),
                offset[1] + (row * cell_size),
                cell_size,
                cell_size
            ))

            if(value and (movement_piece is None or pos != movement_piece.position)):
                x, y = pos.get_pixel_location(offset, board_size, cell_size)
                value.draw(x, y, self.window.surface, cell_size)

        if(movement_piece):
            hovered_cell = None
            try:
                hovered_cell = Coordinate.from_pixel(mouse.get_pos(), offset, board_size)
            except AssertionError:
                ...

            movement_colour = (255, 0, 0)
            dot_size = cell_size * .15

            for move in movement_piece.moves:
                if(hovered_cell is None or hovered_cell != move):
                    draw.circle(
                        surface=self.window.surface,
                        color=movement_colour,
                        center=move.get_pixel_location(
                            offset,
                            board_size, 
                            cell_size
                        ),
                        radius=dot_size
                    )
                else:
                    col, row = move.position
                    draw.rect(
                        self.window.surface,
                        movement_colour,
                        (
                            offset[0] + (col * cell_size),
                            offset[1] + (row * cell_size),
                            cell_size,
                            cell_size
                        )
                    )

            x, y = mouse.get_pos()
            movement_piece.piece.draw(x, y, self.window.surface, cell_size)