import logging

from dataclasses import dataclass
from typing import List
from app.rover_movement.domain.entities.coordinates import Coordinates

from fastapi import APIRouter
from pydantic import BaseModel

from app.rover_movement.application.move_rover.move_rover_command import \
    MoveRoverCommand
from app.rover_movement.application.move_rover.move_rover_handler import \
    MoveRoverHandler
# from app.rover_movement.application.move_rover.move_rover_command import \
#     ComputeNewTargetCommand
# from app.rover_movement.application.move_rover.move_rover_handler import \
#     ComputeNewTargetHandler
# from app.rover_movement.domain.entities.scanned_point import ScannedPoint
# from app.rover_movement.domain.priority_protocols.available_decorator_protocol import \
#     AvailableDecoratorProtocol

logger = logging.getLogger(__name__)

router = APIRouter()


@dataclass
class MovementInput:
    steps: str

class Response(BaseModel):
    coordinates: Coordinates
    direction: str


@router.post("/move", response_model=Response)
async def move_rover(movement_input: MovementInput):

    logger.debug(f'-----> post/move input steps={movement_input}')

    handler = MoveRoverHandler()

    return handler(
        MoveRoverCommand(
            steps=movement_input.steps
        )
    )


@router.get("/status")
async def status():
    return {"message": "Hello World"}