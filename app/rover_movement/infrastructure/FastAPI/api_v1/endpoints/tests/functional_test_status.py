import json
import os
from unittest import TestCase

from fastapi.testclient import TestClient

from app.rover_movement.infrastructure.config import API_V1_STR
from app.rover_movement.infrastructure.FastAPI.main import app


class FunctionalTestMovement(TestCase):
    def setUp(self):
        self._client: TestClient = TestClient(app)
    
    def make_status(self):
        return self._client.get(f"{API_V1_STR}/status")

    def test_status_endpoint(self) -> None:
        endpoint_response = self.make_status()

        self.assertEqual(200, endpoint_response.status_code)

        json_response = endpoint_response.json()

        self.assertEqual(
                "Hello World", json_response["message"]
            )