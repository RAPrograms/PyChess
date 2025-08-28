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
        