from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses.enums import Direction, Team
from dataclasses.units import Coordinate
from .piece import Piece

if TYPE_CHECKING:
    from mvc.model import Model

class Rook(Piece):
    def __init__(self, team: Team):
        super().__init__(team, "Rook")

    def get_valid_movements(self,
        position: Coordinate,
        model: Model,
    ) -> list[Coordinate]:
        output = []
        for dir in [
            Direction.Up,
            Direction.Right,
            Direction.Down,
            Direction.Left
        ]:
            for pos, _ in position.itterate_direction(dir):
                content = model.get_cell(pos)
                if(content is not None and content.team == self.team):
                    break

                output.append(pos)
                if(content is not None):
                    break

                continue

        return output