from dataclasses import dataclass

from app.rover_movement.domain.entities.cardinal_point import CardinalPoint
from app.rover_movement.domain.entities.coordinates import Coordinates


@dataclass
class Rover:
    coordinates: Coordinates
    direction: CardinalPoint

    def move_north(self) -> None:
        self.coordinates.y = Coordinates.increment_between_boundaries(self.coordinates.y)

    def move_west(self) -> None:
        self.coordinates.x = Coordinates.increment_between_boundaries(self.coordinates.x)

    def move_south(self) -> None:
        self.coordinates.y = Coordinates.decrement_between_boundaries(self.coordinates.y)

    def move_east(self) -> None:
        self.coordinates.x = Coordinates.decrement_between_boundaries(self.coordinates.x)

    def move_to_pointing_direction(self, direction) -> None:
        if(direction == CardinalPoint.NORTH):
            self.move_north()
        
        if(direction == CardinalPoint.WEST):
            self.move_west()

        if(direction == CardinalPoint.SOUTH):
            self.move_south()

        if(direction == CardinalPoint.EAST):
            self.move_east()
    
    def rotate_left(self, direction) -> None:
        if(direction == CardinalPoint.NORTH):
            self.direction = CardinalPoint.EAST
        
        if(direction == CardinalPoint.WEST):
            self.direction = CardinalPoint.NORTH

        if(direction == CardinalPoint.SOUTH):
            self.direction = CardinalPoint.WEST

        if(direction == CardinalPoint.EAST):
            self.direction = CardinalPoint.SOUTH

    def rotate_right(self, direction) -> None:
        if(direction == CardinalPoint.NORTH):
            self.direction = CardinalPoint.WEST
        
        if(direction == CardinalPoint.WEST):
            self.direction = CardinalPoint.SOUTH

        if(direction == CardinalPoint.SOUTH):
            self.direction = CardinalPoint.EAST

        if(direction == CardinalPoint.EAST):
            self.direction = CardinalPoint.NORTH

    def __str__(self) -> str:
        return f"Rover(coordinates={self.coordinates}, direction={self.direction})"
