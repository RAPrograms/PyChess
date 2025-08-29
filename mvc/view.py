from typing import Any, Generator
from pygame import locals, draw

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
        self.window.add_event(locals.MOUSEMOTION, instance.handle_mouse_movement)
        self.window.add_event(locals.VIDEORESIZE, instance.handle_resize)


    def draw(self, data: Generator[tuple[Coordinate, None | Rook | Knight | Bishop | King | Queen | Bishop | Knight | Rook | Pawn], Any, None]):
        self.window.surface.fill((0,0,0))

        board_size = self.window.smallest_boundary
        half_board = board_size / 2
        cell_size = board_size / 8

        offset = self.window.screen_center
        offset[0] -= half_board
        offset[1] -= half_board

        for pos, value in data:
            col, row = pos.position
            colour = cWhite if (pos.index + (row % 2)) % 2 == 0 else cBlack

            draw.rect(self.window.surface, colour, (
                offset[0] + (col * cell_size),
                offset[1] + (row * cell_size),
                cell_size,
                cell_size
            ))

            if(value):
                value.draw(offset, pos, self.window.surface, cell_size)