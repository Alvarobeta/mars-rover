import logging

from typing import ClassVar, Dict, List

from app.rover_movement.domain.move_rover.available_decorator_movement import \
    AvailableDecoratorMovement
from app.rover_movement.domain.move_rover.movement_interface import \
    MovementInterface
from app.rover_movement.domain.move_rover.move_forward_rover import \
    MoveForwardRover
from app.rover_movement.domain.move_rover.rotate_rover_left import \
    RotateRoverLeft
from app.rover_movement.domain.move_rover.rotate_rover_right import \
    RotateRoverRight


logger = logging.getLogger(__name__)

class FactoryMovement:
    MOVEMENT_MAP: ClassVar[Dict] = {
        AvailableDecoratorMovement.FORWARD: MoveForwardRover,
        AvailableDecoratorMovement.LEFT: RotateRoverLeft,
        AvailableDecoratorMovement.RIGHT: RotateRoverRight
    }

    def build(
        self,
        movements_to_add: List[AvailableDecoratorMovement],
    ) -> MovementInterface:
        movement_to_decorate = None

        logger.debug(f'-----> movement_to_decorate={movement_to_decorate}')
        logger.debug(f'-----> movements_to_add={movements_to_add}')

        for p in movements_to_add:

            logger.debug(f'-----> movement to add (p)={p}')

            movement_to_decorate = self.MOVEMENT_MAP[p](movement_to_decorate)

        logger.debug(f'-----> movement_to_decorate before return={movement_to_decorate}')

        return movement_to_decorate
