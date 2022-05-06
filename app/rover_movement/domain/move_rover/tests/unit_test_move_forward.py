import logging
import json
import os

from unittest import TestCase

from app.rover_movement.domain.entities.cardinal_point import \
    CardinalPoint
from app.rover_movement.domain.entities.coordinates import \
    Coordinates
from app.rover_movement.domain.entities.rover import \
    Rover
from app.rover_movement.domain.entities.steps import \
    Steps

from app.rover_movement.domain.move_rover.move_forward_rover import \
    MoveForwardRover
from app.rover_movement.domain.move_rover.tests.rover_mother import \
    RoverMother


logger = logging.getLogger(__name__)

class UnitTestMoveForward(TestCase):
    def setUp(self):
        self.move_forward = MoveForwardRover()
        self.initial_rover = RoverMother.build(
            cardinal_point=CardinalPoint.NORTH,
            coordinate_x=0,
            coordinate_y=0
        )

    def test_move(self):
        final_position = RoverMother.build(
            cardinal_point=CardinalPoint.NORTH,
            coordinate_x=0,
            coordinate_y=1
            )
        
        result = self.move_forward.move(self.initial_rover)

        self.assertEqual(final_position, result)

    def test_move_boundaries(self):
        initial_position = RoverMother.build(
            cardinal_point=CardinalPoint.NORTH,
            coordinate_x=0,
            coordinate_y=9
        )

        final_position = RoverMother.build(
            cardinal_point=CardinalPoint.NORTH,
            coordinate_x=0,
            coordinate_y=0
        )

        result = self.move_forward.move(initial_position)

        self.assertEqual(final_position, result)
