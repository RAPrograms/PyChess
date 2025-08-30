from __future__ import annotations
from typing import TYPE_CHECKING

from classes.enums import RelativeDirection, Team
from classes.units import Coordinate
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
            return self.create_direction_paths(position, model, [forward_dir], 2)
       
        output = []

        ##Forward
        forward_pieces = model.get_pieces_in_direction(position, forward_dir, 1)
        if(len(forward_pieces) > 0 and forward_pieces[0] == None):
            pos = position.move(forward_dir)
            if(pos is not None):
                output.append(pos)
       
        #Side Captures
        for dir in [RelativeDirection.ForwardLeft, RelativeDirection.ForwardRight]:
            abs_dir = self.make_direction_absolute(dir)

            path = model.get_pieces_in_direction(position, abs_dir, 2)
            if(len(path) <= 0 or path[0] is None):
                continue
            
            if(path[0].team == self.team):
                continue

            if(len(path) > 1):
                if(path[1] is not None):
                    continue
       
            pos = position.move(abs_dir)
            output.append(pos)

        return output