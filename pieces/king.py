from .piece import Piece
from enums import Team

class King(Piece):
    def __init__(self, team: Team):
        super().__init__(team, "King")