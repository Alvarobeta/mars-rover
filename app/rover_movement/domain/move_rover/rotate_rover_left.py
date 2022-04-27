from app.rover_movement.domain.entities.rover import Rover

from app.rover_movement.domain.move_rover.movement_base_decorator import \
    MovementBaseDecorator


class RotateRoverLeft(MovementBaseDecorator):
    def move(
        self, rover: Rover
    ) -> Rover:

        rover.rotate_left(rover.direction)
        
        if super().movement_wrapped:
            return super().movement_wrapped.move(rover)
        
        return rover
