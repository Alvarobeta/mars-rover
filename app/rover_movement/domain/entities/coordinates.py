import math
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Coordinates:
    x: int
    y: int

    MAX_DISTANCE: ClassVar[int] = 9
    MIN_DISTANCE: ClassVar[int] = 0

    def increment_between_boundaries(gridPoint) -> int:
        if (gridPoint + 1 > Coordinates.MAX_DISTANCE):
            return Coordinates.MIN_DISTANCE
        else:
            return gridPoint + 1
      
    def decrement_between_boundaries(gridPoint) -> int:
        if (gridPoint - 1 < Coordinates.MIN_DISTANCE):
            return Coordinates.MAX_DISTANCE
        else:
            return gridPoint - 1

    def __str__(self) -> str:
        return f"Coordinates(x={self.x}, y={self.y})"
