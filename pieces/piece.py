from typing import Literal

from pygame import Surface, image as gameImage, transform as gameTransform

from dataclasses.enums import Team
from dataclasses.units import Coordinate

class Piece:
    def __init__(self, team: Team, type: Literal["Bishop", "King", "Knight", "Pawn", "Queen", "Rook"]):
        self.team = team

        self.image = gameImage.load(f"./assets/{team.value}/{type}.png")

    def draw(self, offset: list[int], position: Coordinate, display: Surface, size: int):
        col, row = position.position

        img_size = size - 10
        img = gameTransform.scale(self.image, (img_size, img_size))

        center_offset = (size / 2) - (img_size / 2)

        display.blit(img, (
            offset[0] + (col * size) + center_offset,
            offset[1] + (row * size) + center_offset,
        ))

    def get_side_distance(self, position: Coordinate):
        """
        Returns the rows from the team's side

        White side is the top and Black's is the bottom
        """
        if self.team == Team.White:
            return position.row + 1
        return 8 - position.row

    def get_valid_movements(self, position: Coordinate) -> list[Coordinate]:
        raise NotImplemented
