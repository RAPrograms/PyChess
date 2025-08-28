from typing import Any

from units import Coordinate

class Model:
    _board: list[Any]

    def __init__(self):
        self.reset_board()

    def reset_board(self):
        self._board = []
        for _ in self.itterate_board():
            self._board.append(None)


    def itterate_board(self):
        for i in range(64):
            coordinate = Coordinate(i)
            try:
                yield (coordinate, self._board[i])
            except IndexError:
                yield (coordinate, None)
        