import logging
import json
import os
from unittest import TestCase
from app.rover_movement.domain.entities.coordinates import Coordinates
from app.rover_movement.domain.entities.rover import Rover

from fastapi.testclient import TestClient

from app.rover_movement.infrastructure.config import API_V1_STR
from app.rover_movement.infrastructure.FastAPI.main import app

logger = logging.getLogger(__name__)

class FunctionalTestMovement(TestCase):
    def setUp(self):
        self._client: TestClient = TestClient(app)

    def make_request(self, json_data):
        return self._client.post(f"{API_V1_STR}/move", json=json_data)

    def test_valid_requests(self) -> None:
        TEST_DATA = "test_movement_valid_requests.json"

        test_data_path = os.path.dirname(os.path.abspath(__file__)) + "/" + TEST_DATA
        data = json.load(open(test_data_path))
        
        logger.debug(f'------- test data = {data}')
        
        for r in data:
            
            logger.debug(f'------- test data in for = {r}')
            logger.debug(f'------- test request = {r["request"]}')
            logger.debug(f'------- test response = {r["response"]}')

            endpoint_response = self.make_request(r["request"])

            assert endpoint_response.status_code == 200
            assert endpoint_response.json() == r["response"]