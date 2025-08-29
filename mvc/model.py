from typing import Any, Generator

from dataclasses.moving_event import MovingEvent
from dataclasses.enums import Direction, RelativeDirection, Team
from dataclasses.units import Coordinate

from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.king import King

class Model:
    _board: list[Bishop | Knight | Queen | Rook | Pawn | King | None]

    _moving_piece: MovingEvent | None

    def __init__(self):
        self.clear_board()
        self.setup_pieces()
        self._moving_piece = None
        

    def clear_board(self):
        self._board = []
        for _ in self.itterate_board():
            self._board.append(None)
        

    def set_cell(
        self,
        position: Coordinate,
        value: None | Rook | Knight | Bishop | King | Queen | Bishop | Knight | Rook | Pawn
    ):
        self._board[position.index] = value
        

    def get_cell(self, position: Coordinate) -> None | Rook | Knight | Bishop | King | Queen | Bishop | Knight | Rook | Pawn:
        try:
            return self._board[position.index]
        except IndexError:
            return None


    def setup_pieces(self):
        for i, piece in enumerate([Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]):
            self.set_cell(Coordinate.from_position(i, 0), piece(Team.White))
            self.set_cell(Coordinate.from_position(i, 7), piece(Team.Black))

        for i in range(8):
            self.set_cell(Coordinate.from_position(i, 1), Pawn(Team.White))
            self.set_cell(Coordinate.from_position(i, 6), Pawn(Team.Black))
            

    def get_pieces_in_direction(
        self,
        start_position: Coordinate,
        direction: Direction,
        distance: int = 7,
        include_start: bool = False
    ) -> list[None | Rook | Knight | Bishop | King | Queen | Bishop | Knight | Rook | Pawn]:
        pos = start_position
        output = []
        if(include_start):
            contents = self.get_cell(pos)
            output.append(contents)
            distance -= 1

        for _ in range(distance):
            pos = pos.move(direction)
            if(pos is None):
                break
            
            contents = self.get_cell(pos)
            output.append(contents)

        return output


    def itterate_board(self) -> Generator[tuple[Coordinate, None | Rook | Knight | Bishop | King | Queen | Bishop | Knight | Rook | Pawn], Any, None]:
        for i in range(64):
            coordinate = Coordinate(i)
            try:
                yield (coordinate, self._board[i])
            except IndexError:
                yield (coordinate, None)


    def move_piece(self, original: Coordinate, new: Coordinate):
        contents = self.get_cell(original)
        self.set_cell(original, None)
        self.set_cell(new, contents)
        

    @property
    def movement_piece(self):
        return self._moving_piece


    def start_piece_movement(self, movement: MovingEvent):
        self._moving_piece = movement


    def end_piece_movement(self):
        self._moving_piece = None