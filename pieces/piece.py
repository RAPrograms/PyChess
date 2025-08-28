from typing import Literal
from enums import Team

from pygame import Surface, image as gameImage, transform as gameTransform

from units import Coordinate

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