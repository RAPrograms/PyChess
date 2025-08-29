from math import floor

from pygame.event import Event

from dataclasses.enums import Direction

class Coordinate:
    def __init__(self, index: int):
        self._index = index

    @classmethod
    def from_position(self, column: int, row: int):
        assert 0 <= column and column < 8, f"Column out of board ({column})"
        assert 0 <= row and row < 8, f"Row out of board ({row})"

        return self((row * 8) + column)
    
    @classmethod
    def from_pixel(self, event: Event, bondary_start: list[int], size: int):
        x, y = event.pos
        
        assert bondary_start[0] <= x and bondary_start[1] <= y, "Pixel out of board bounds"
        assert x <= (bondary_start[0] + size) and y <= (bondary_start[1] + size), "Pixel out of board bounds"
         
        x -= bondary_start[0]
        y -= bondary_start[1]

        cell_size = size / 8

        column = floor(x / cell_size)
        row = floor(y / cell_size)

        return Coordinate.from_position(column, row)

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
    
    def get_pixel_location(self, bondary_start: list[int], bondary_size: int, cell_size: int):
        col, row = self.position
        half_size = cell_size / 2

        return [
            bondary_start[0] + (col * cell_size) + half_size,
            bondary_start[1] + (row * cell_size) + half_size
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
    
    def __eq__(self, other):
        return self.index == other.index

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        position = self.position
        return f"<Position: [{position[0]}, {position[1]}] | Index: {self.index} >"