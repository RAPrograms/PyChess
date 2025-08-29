from dataclasses.enums import Direction

class Coordinate:
    def __init__(self, index: int):
        self._index = index

    @classmethod
    def from_position(self, column: int, row: int):
        assert 0 <= column and column < 8, f"Column out of board ({column})"
        assert 0 <= row and row < 8, f"Row out of board ({row})"

        return self((row * 8) + column)

    @property
    def index(self):
        return self._index
    
    @property
    def position(self):
        """Returns the [column, row] from index"""
        column = self._index % 8
        row = self._index // 8

        return [
            column,
            row
        ]
    
    @property
    def column(self):
        return self.position[0]

    @property
    def row(self):
        return self.position[1]
        
    def is_valid(self):
        col, row = self.position

        if(col < 0 or row < 0):
            return False
        
        if(col >= 8 or row >= 8):
            return False
        
        return True

    def move(self, direction: Direction):
        velocity = (direction.value[1] * 8) + direction.value[0]
        return Coordinate(self.index + velocity)