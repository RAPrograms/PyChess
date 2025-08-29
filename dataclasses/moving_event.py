from dataclasses.units import Coordinate

from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.king import King

class MovingEvent:
    def __init__(
        self,
        piece: Rook | Knight | Bishop | King | Queen | Bishop | Knight | Pawn,
        position: Coordinate 
    ):
        self._piece = piece
        self._position = position

    @property
    def piece(self):
        return self._piece
    
    @property
    def position(self):
        return self._position