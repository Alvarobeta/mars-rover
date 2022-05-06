import logging

from typing import List
from app.rover_movement.domain.entities.coordinates import Coordinates
from app.rover_movement.domain.entities.rover import Rover
from app.rover_movement.domain.entities.steps import Steps

from app.rover_movement.domain.move_rover.factory_movement import \
    FactoryMovement
from app.rover_movement.domain.move_rover.movement_interface import \
    MovementInterface

logger = logging.getLogger(__name__)


class RoverMoverService:
    def __init__(self, steps: Steps):
        self._factory_movement = FactoryMovement()
        
        logger.debug(f'-----> factory_movement={self._factory_movement}')
        
        self._movement = self._build_movement(steps)

    def _build_movement(
        self, steps: Steps
    ) -> MovementInterface:
        return self._factory_movement.build(movements_to_add=steps)

    def move_to_next_position(
        self, rover: Rover
    ) -> Rover:
        rover_after_move = self._movement.move(rover)

        return rover_after_move
