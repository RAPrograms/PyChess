from .piece import Piece
from dataclasses.enums import Team

class Pawn(Piece):
    def __init__(self, team: Team):
        super().__init__(team, "Pawn")