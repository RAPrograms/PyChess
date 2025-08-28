from typing import Literal
from enums import Team

from pygame import Surface, image as gameImage, transform as gameTransform

class Piece:
    def __init__(self, team: Team, type: Literal["Bishop", "King", "Knight", "Pawn", "Queen", "Rook"]):
        self.team = team

        self.image = gameImage.load(f"./assets/{team.value}/{type}.png")
        self.image = gameTransform.scale(self.image, (70, 70))

    def draw(self, row: int, col: int, display: Surface, tile_size: int = 75):
        screen_x = col * tile_size
        screen_y = row * tile_size
        display.blit(self.image, (screen_x, screen_y))