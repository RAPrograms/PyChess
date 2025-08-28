from pygame import locals, draw

from window import Window
from model import Model

class View:
    def __init__(self, window: Window, model: Model):
        self.window = window
        self.window.add_event(locals.VIDEORESIZE, lambda _: self.draw())

        self.model = model

        self.draw()

    def draw_checkerboard(self, start: list[int], size: int):
        cell_size = size / 8

        cWhite = (255, 255, 255)
        cBlack = (0,255,0)

        for pos, _ in self.model.itterate_board():
            col, row = pos.position
            colour = cWhite if (pos.index + (row % 2)) % 2 == 0 else cBlack

            draw.rect(self.window.surface, colour, (
                start[0] + (col * cell_size),
                start[1] + (row * cell_size),
                cell_size,
                cell_size
            ))


    def draw(self):
        self.window.surface.fill((0,0,0))

        board_size = self.window.smallest_boundary
        half_board = board_size / 2

        offset = self.window.screen_center
        offset[0] -= half_board
        offset[1] -= half_board

        self.draw_checkerboard(offset, board_size)