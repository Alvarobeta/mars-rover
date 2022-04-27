from abc import ABC, abstractmethod

from app.rover_movement.domain.entities.rover import Rover


class MovementInterface(ABC):
    @abstractmethod
    def move(
        self, rover: Rover
    ) -> Rover:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
