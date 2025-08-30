from __future__ import annotations
from typing import Literal, TYPE_CHECKING

from pygame import Surface, image as gameImage, transform as gameTransform

from classes.enums import RelativeDirection, Team, Direction
from classes.units import Coordinate

if TYPE_CHECKING:
    from mvc.model import Model

class Piece:
    def __init__(self, team: Team, type: Literal["Bishop", "King", "Knight", "Pawn", "Queen", "Rook"]):
        self.team = team

        self.image = gameImage.load(f"./assets/{team.value}/{type}.png")

    def draw(self, x: int, y: int, display: Surface, size: int):
        img_size = size - 10
        img = gameTransform.scale(self.image, (img_size, img_size))

        half_size = img_size / 2
        display.blit(img, (
            x - half_size,
            y - half_size
        ))

    def get_side_distance(self, position: Coordinate):
        """
        Returns the rows from the team's side

        White side is the top and Black's is the bottom
        """
        if self.team == Team.White:
            return position.row + 1
        return 8 - position.row

    def make_direction_absolute(self, direction: RelativeDirection):
        if(self.team == Team.Black):
            return Direction(direction.value)
        
        horizontal, vertical = direction.value
        
        horizontal *= -1
        vertical *= -1
        
        return Direction((horizontal, vertical))
    
    def create_direction_paths(
        self,
        position: Coordinate,
        model: Model,
        directions: list[Direction],
        distance: int = None
    ):
        output = []
        for dir in directions:
            for pos, i in position.itterate_direction(dir):
                if(distance and distance <= i):
                    break
                
                content = model.get_cell(pos)
                if(content is not None and content.team == self.team):
                    break

                output.append(pos)
                if(content is not None):
                    break

                continue

        return output

    def get_valid_movements(self, position: Coordinate, model: Model) -> list[Coordinate]:
        raise NotImplemented

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"<{self.__class__.__name__}>"