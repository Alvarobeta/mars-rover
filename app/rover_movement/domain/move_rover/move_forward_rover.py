from app.rover_movement.domain.entities.rover import Rover

from app.rover_movement.domain.move_rover.movement_base_decorator import \
    MovementBaseDecorator


class MoveForwardRover(MovementBaseDecorator):
    def move(
        self, rover: Rover
    ) -> Rover:
        rover.move_to_pointing_direction(rover.direction)

        if super().movement_wrapped:
            return super().movement_wrapped.move(rover)
        
        return rover
