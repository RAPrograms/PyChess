from enum import Enum

class Team(Enum):
    Black = "Black"
    White = "White"

class Direction(Enum):
    UpLeft = (-1, -1)
    Up = (0, -1)
    UpRight = (1, -1)
    Right = (1, 0)
    DownRight = (1, 1)
    Down = (0, 1)
    DownLeft = (-1, 1)
    Left = (-1, 0)

class RelativeDirection(Enum):
    ForwardLeft = (-1, -1)
    Forward = (0, -1)
    ForwardRight = (1, -1)
    Right = (1, 0)
    BackwardsRight = (1, 1)
    Backwards = (0, 1)
    BackwardsLeft = (-1, 1)
    Left = (-1, 0)