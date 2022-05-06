import random

from app.rover_movement.domain.entities.cardinal_point import CardinalPoint
from app.rover_movement.domain.entities.coordinates import Coordinates
from app.rover_movement.domain.entities.rover import Rover

class RoverMother:
    @staticmethod
    def build(
        coordinate_x: int = random.randint(0, 100),
        coordinate_y: int = random.randint(0, 100),
        cardinal_point: CardinalPoint = random.choice(list(CardinalPoint)),
    ):

        return Rover(
            coordinates=Coordinates(x=coordinate_x, y=coordinate_y),
            direction=cardinal_point,
        )