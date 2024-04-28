import unittest
from fastapi.testclient import TestClient
from app import app

class TestAPI(unittest.TestCase):
    """Test cases for the FastAPI endpoints."""

    def setUp(self):
        self.client = TestClient(app)

    def test_get_daily_avg_aqi_success(self):
        """
        Test case for successful response of /api/aqi/avg/daily endpoint.
        """
        response = self.client.get("/api/aqi/avg/daily")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())
    
    def test_get_day_aqi_success(self):
        """
        Test case for successful response of /api/aqi/day/{day_id} endpoint.
        """
        # Assume day_id for Monday is 2
        day_id = 2
        response = self.client.get(f"/api/aqi/day/{day_id}")
        self.assertEqual(response.status_code, 200)
    
    def test_get_daily_avg_aqi_empty_database(self):
        """
        Test case for /api/aqi/avg/daily endpoint with not empty database.
        """
        response = self.client.get("/api/aqi/avg/daily")
        self.assertEqual(response.status_code, 200)        
        self.assertNotEqual(response.json(), [])
    
    def test_get_day_aqi_non_empty_database(self):
        """
        Test case for /api/aqi/day/{day_id} endpoint with not empty database.
        """
        # Assume day_id for Monday is 2
        day_id = 2
        response = self.client.get(f"/api/aqi/day/{day_id}")
        self.assertEqual(response.status_code, 200)        
        self.assertNotEqual(response.json(), [])
    
    def test_get_daily_avg_aqi_database_error(self):
        """
        Test case for database error handling in /api/aqi/avg/daily endpoint.
        """
        response = self.client.get("/api/aqi/avg/daily")
        self.assertEqual(response.status_code, 500)
        


if __name__ == '__main__':
    unittest.main()
