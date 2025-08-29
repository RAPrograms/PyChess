from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses.units import Coordinate
from dataclasses.enums import Direction, Team
from .piece import Piece

if TYPE_CHECKING:
    from mvc.model import Model

class Pawn(Piece):
    def __init__(self, team: Team):
        super().__init__(team, "Pawn")

    def get_valid_movements(self,
        position: Coordinate,
        model: Model,
    ) -> list[Coordinate]:
        


        return [
            Coordinate.from_position(0, 5),
            Coordinate.from_position(0, 4),
        ]