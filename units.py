class Coordinate:
    def __init__(self, index: int):
        self._index = index

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
        