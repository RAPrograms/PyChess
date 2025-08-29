from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses.enums import Direction, Team
from dataclasses.units import Coordinate
from .piece import Piece

if TYPE_CHECKING:
    from mvc.model import Model

class Knight(Piece):
    def __init__(self, team: Team):
        super().__init__(team, "Knight")

    def _get_side_positions(self, direction: Direction):
        one = Direction((direction.value[1], direction.value[0]))
        two = Direction((one.value[0] * -1, one.value[1] * -1))

        return [one, two]


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
            line_pos = position.move(dir, 2)
            if(line_pos is None):
                continue

            for rotated_dir in self._get_side_positions(dir):
                pos = line_pos.move(rotated_dir)
                if(pos is None):
                    continue

                content = model.get_cell(pos)
                if(content is None):
                    output.append(pos)
                    continue

                if(content.team != self.team):
                    output.append(pos)

        return output