from abc import ABC

from app.rover_movement.domain.move_rover.movement_interface import \
    MovementInterface


class MovementBaseDecorator(MovementInterface, ABC):
    def __init__(self, movement_wrapped: MovementInterface = None):
        self._movement_wrapped = movement_wrapped

    @property
    def movement_wrapped(self) -> MovementInterface:
        return self._movement_wrapped

    def __str__(self) -> str:
        return self.__class__.__name__ + "(" + str(self._movement_wrapped) + ")"
