from dataclasses import dataclass
from app.rover_movement.domain.entities.steps import Steps


@dataclass
class MoveRoverCommand:
    steps: Steps
