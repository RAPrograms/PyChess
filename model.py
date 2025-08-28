from typing import Any, Generator

from units import Coordinate
from enums import Team

from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.king import King

class Model:
    _board: list[Any]

    def __init__(self):
        self.clear_board()
        self.setup_pieces()


    def clear_board(self):
        self._board = []
        for _ in self.itterate_board():
            self._board.append(None)
        
    def set_cell(
        self,
        position: Coordinate,
        value: None | Rook | Knight | Bishop | King | Queen | Bishop | Knight | Rook
    ):
        self._board[position.index] = value


    def setup_pieces(self):
        for i, piece in enumerate([Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]):
            self.set_cell(Coordinate.from_position(i, 0), piece(Team.White))
            self.set_cell(Coordinate.from_position(i, 7), piece(Team.Black))

        for i in range(8):
            self.set_cell(Coordinate.from_position(i, 1), Pawn(Team.White))
            self.set_cell(Coordinate.from_position(i, 6), Pawn(Team.Black))
            


    def itterate_board(self) -> Generator[tuple[Coordinate, None | Rook | Knight | Bishop | King | Queen | Bishop | Knight | Rook], Any, None]:
        for i in range(64):
            coordinate = Coordinate(i)
            try:
                yield (coordinate, self._board[i])
            except IndexError:
                yield (coordinate, None)
        