from enum import Enum


class CardinalPoint(str, Enum):
    NORTH = "N"
    WEST = "W"
    EAST = 'E'
    SOUTH = 'S'

    def __str__(self) -> str:
        return self.value
