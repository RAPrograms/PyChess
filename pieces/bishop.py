from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses.enums import Direction, Team
from dataclasses.units import Coordinate
from .piece import Piece

if TYPE_CHECKING:
    from mvc.model import Model

class Bishop(Piece):
    def __init__(self, team: Team):
        super().__init__(team, "Bishop")

    def get_valid_movements(self,
        position: Coordinate,
        model: Model,
    ) -> list[Coordinate]:
        return self.create_direction_paths(position, model, [
            Direction.UpLeft,
            Direction.UpRight,
            Direction.DownLeft,
            Direction.DownRight
        ])