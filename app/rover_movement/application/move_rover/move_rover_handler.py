import logging

from app.rover_movement.application.move_rover.move_rover_command import \
    MoveRoverCommand

from app.rover_movement.domain.entities.rover import Rover
from app.rover_movement.domain.entities.coordinates import Coordinates
from app.rover_movement.domain.rover_mover_service import \
    RoverMoverService

logger = logging.getLogger(__name__)

class MoveRoverHandler:
    def __call__(self, command: MoveRoverCommand) -> Rover:

        logger.debug(f'-----> Command={command.steps}')

        rover = Rover(
            coordinates=Coordinates(x=0,y=0),
            direction='N'
        )

        rover_mover = RoverMoverService(steps=command.steps[::-1])

        logger.debug(f'-----> rover_mover={rover_mover}')

        return rover_mover.move_to_next_position(rover) 
