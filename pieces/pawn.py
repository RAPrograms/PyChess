from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses.enums import Direction, RelativeDirection, Team
from dataclasses.units import Coordinate
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
        forward_dir = self.make_direction_absolute(RelativeDirection.Forward)

        #Handles first move
        if(self.get_side_distance(position) == 2):
            return position.create_move_path(forward_dir)
       
        output = []

        #Forward
        forward_pieces = model.get_pieces_in_direction(position, forward_dir, 1)
        if(forward_pieces[0] == None):
            output.append(position.move(forward_dir))

        

        return output