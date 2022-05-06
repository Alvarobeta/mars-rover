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