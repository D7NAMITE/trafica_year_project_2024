import unittest
from fastapi.testclient import TestClient
from app import app

class TestAPI(unittest.TestCase):
    """Test cases for the FastAPI endpoints."""

    def setUp(self):
        self.client = TestClient(app)
    
    def test_get_avg_aqi_success(self):
        """
        Test case for successful response of /api/aqi/avg endpoint.
        """
        response = self.client.get("/api/aqi/avg")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())

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
    
    def test_get_min_aqi_us_success(self):
        """
        Test case for successful response of /api/aqi/min/aqi_us endpoint.
        """
        response = self.client.get("/api/aqi/min/aqi_us")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())
    
    def test_get_max_aqi_us_success(self):
        """
        Test case for successful response of /api/aqi/max/aqi_us endpoint.
        """
        response = self.client.get("/api/aqi/max/aqi_us")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())
    
    def test_get_min_pm25_success(self):
        """
        Test case for successful response of /api/aqi/min/pm25 endpoint.
        """
        response = self.client.get("/api/aqi/min/pm25")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())
    
    def test_get_max_pm25_success(self):
        """
        Test case for successful response of /api/aqi/max/pm25 endpoint.
        """
        response = self.client.get("/api/aqi/max/pm25")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())
    
    def test_get_noise_aqi_success(self):
        """
        Test case for successful response of /api/noise/avg endpoint.
        """
        response = self.client.get("/api/noise/avg")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())

    def test_get_daily_avg_noise_success(self):
        """
        Test case for successful response of /api/noise/avg/daily endpoint.
        """
        response = self.client.get("/api/noise/avg/daily")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())
    
    def test_get_min_noise_success(self):
        """
        Test case for successful response of /api/noise/min endpoint.
        """
        response = self.client.get("/api/noise/min")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())
    
    def test_get_max_noise_success(self):
        """
        Test case for successful response of /api/noise/max endpoint.
        """
        response = self.client.get("/api/noise/max")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())

    def test_get_day_noise_success(self):
        """
        Test case for successful response of /api/noise/day/{day_id} endpoint.
        """
        # Assume day_id for Tuesday is 3
        day_id = 3
        response = self.client.get(f"/api/noise/day/{day_id}")
        self.assertEqual(response.status_code, 200)
    
    def test_get_avg_traffic_success(self):
        """
        Test case for successful response of /api/traffic/avg endpoint.
        """
        response = self.client.get("/api/traffic/avg")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())
    
    def test_get_daily_avg_traffic_success(self):
        """
        Test case for successful response of /api/traffic/avg/daily endpoint.
        """
        response = self.client.get("/api/traffic/avg/daily")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())
    
    def test_get_day_traffic_success(self):
        """
        Test case for successful response of /api/traffic/day/{day_id} endpoint.
        """
        # Assume day_id for Monday is 2
        day_id = 2
        response = self.client.get(f"/api/traffic/day/{day_id}")
        self.assertEqual(response.status_code, 200)

    def test_get_road_traffic_success(self):
        """
        Test case for successful response of /api/traffic/road/{road_id} endpoint.
        """
        # Assume road_id for ngamwongwan road is 2
        road_id = 2
        response = self.client.get(f"/api/traffic/road/{road_id}")
        self.assertEqual(response.status_code, 200)
    
    def test_get_min_traffic_success(self):
        """
        Test case for successful response of /api/traffic/min endpoint.
        """
        response = self.client.get(f"/api/traffic/min")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json())
    
    def test_get_avg_aqi_non_empty_database(self):
        """
        Test case for /api/aqi/avg endpoint with not empty database.
        """
        response = self.client.get("/api/aqi/avg")
        self.assertEqual(response.status_code, 200)        
        self.assertNotEqual(response.json(), [])

    def test_get_daily_avg_aqi_non_empty_database(self):
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
    
    def test_get_min_aqi_us_non_empty_database(self):
        """
        Test case for /api/aqi/min/aqi_us endpoint with not empty database.
        """
        response = self.client.get(f"/api/aqi/min/aqi_us")
        self.assertEqual(response.status_code, 200)        
        self.assertNotEqual(response.json(), [])
    
    def test_get_max_aqi_us_non_empty_database(self):
        """
        Test case for /api/aqi/max/aqi_us endpoint with not empty database.
        """
        response = self.client.get(f"/api/aqi/max/aqi_us")
        self.assertEqual(response.status_code, 200)        
        self.assertNotEqual(response.json(), [])
    
    def test_get_min_pm25_non_empty_database(self):
        """
        Test case for /api/aqi/min/pm25 endpoint with not empty database.
        """
        response = self.client.get(f"/api/aqi/min/pm25")
        self.assertEqual(response.status_code, 200)        
        self.assertNotEqual(response.json(), [])
    
    def test_get_max_pm25_non_empty_database(self):
        """
        Test case for /api/aqi/max/pm25 endpoint with not empty database.
        """
        response = self.client.get(f"/api/aqi/max/pm25")
        self.assertEqual(response.status_code, 200)        
        self.assertNotEqual(response.json(), [])
    
    def test_get_daily_avg_noise_non_empty_database(self):
        """
        Test case for /api/noise/avg/daily endpoint with not empty database.
        """
        response = self.client.get("/api/noise/avg/daily")
        self.assertEqual(response.status_code, 200)        
        self.assertNotEqual(response.json(), [])
    
    def test_get_day_noise_non_empty_database(self):
        """
        Test case for /api/noise/day/{day_id} endpoint with not empty database.
        """
        # Assume day_id for Tuesday is 3
        day_id = 3
        response = self.client.get(f"/api/noise/day/{day_id}")
        self.assertEqual(response.status_code, 200)        
        self.assertNotEqual(response.json(), [])
    
    def test_get_daily_avg_traffic_non_empty_database(self):
        """
        Test case for /api/traffic/avg/daily endpoint with not empty database.
        """
        response = self.client.get("/api/traffic/avg/daily")
        self.assertEqual(response.status_code, 200)        
        self.assertNotEqual(response.json(), [])
    
    def test_get_day_traffic_non_empty_database(self):
        """
        Test case for /api/traffic/day/{day_id} endpoint with not empty database.
        """
        # Assume day_id for Monday is 2
        day_id = 2
        response = self.client.get(f"/api/traffic/day/{day_id}")
        self.assertEqual(response.status_code, 200)        
        self.assertNotEqual(response.json(), [])

    def test_get_road_traffic_non_empty_database(self):
        """
        Test case for /api/traffic/road/{road_id} endpoint with not empty database.
        """
        # Assume road_id for ngamwongwan is 2
        road_id = 2
        response = self.client.get(f"/api/traffic/road/{road_id}")
        self.assertEqual(response.status_code, 200)        
        self.assertNotEqual(response.json(), [])

    def test_get_daily_avg_aqi_database_error(self):
        """
        Test case for database error handling in /api/aqi/avg/daily endpoint.
        """
        response = self.client.get("/api/aqi/avg/daily")
        self.assertEqual(response.status_code, 500)
    
    def test_get_day_aqi_database_error(self):
        """
        Test case for database error handling in /api/aqi/day/{day_id} endpoint.
        """
        # Assume day_id for Monday is 2
        day_id = 2
        response = self.client.get(f"/api/aqi/day/{day_id}")
        self.assertEqual(response.status_code, 500)
    
    def test_get_daily_avg_noise_database_error(self):
        """
        Test case for database error handling in /api/noise/avg/daily endpoint.
        """
        response = self.client.get("/api/noise/avg/daily")
        self.assertEqual(response.status_code, 500)
    
    def test_get_day_noise_database_error(self):
        """
        Test case for database error handling in /api/noise/day/{day_id} endpoint.
        """
        # Assume day_id for Tuesday is 3
        day_id = 3
        response = self.client.get(f"/api/noise/day/{day_id}")
        self.assertEqual(response.status_code, 500)
    
    def test_get_daily_avg_traffic_database_error(self):
        """
        Test case for database error handling in /api/traffic/avg/daily endpoint.
        """
        response = self.client.get("/api/traffic/avg/daily")
        self.assertEqual(response.status_code, 500)
    
    def test_get_day_traffic_database_error(self):
        """
        Test case for database error handling in /api/traffic/day/{day_id} endpoint.
        """
        # Assume day_id for Monday is 2
        day_id = 2
        response = self.client.get(f"/api/traffic/day/{day_id}")
        self.assertEqual(response.status_code, 500)
    
    def test_get_road_traffic_database_error(self):
        """
        Test case for database error handling in /api/traffic/road/{road_id} endpoint.
        """
        # Assume road_id for ngamwongwan is 2
        road_id = 2
        response = self.client.get(f"/api/traffic/road/{road_id}")
        self.assertEqual(response.status_code, 500)

    def test_valid_road_ids(self):
        """Test with valid road_id values within the range 1 to 3."""
        valid_road_ids = [1, 2, 3]
        for road_id in valid_road_ids:
            with self.subTest(road_id=road_id):
                response = self.client.get(f"/api/traffic/road/{road_id}")
                self.assertEqual(response.status_code, 200)
    
    def test_invalid_road_ids(self):
        """Test with invalid road_id values."""
        invalid_road_ids = [0, 4, -1]
        for road_id in invalid_road_ids:
            with self.subTest(road_id=road_id):
                response = self.client.get(f"/api/traffic/road/{road_id}")
                self.assertEqual(response.status_code, 404)
        
         # Test with non-integer road_id value
        response = self.client.get("/api/traffic/road/helloworld")
        self.assertEqual(response.status_code, 422)
    
    def test_valid_day_ids(self):
        """Test with valid day_id values within the range 1 to 7."""
        valid_day_ids = [1, 2, 3, 4, 5, 6, 7]
        for day_id in valid_day_ids:
            with self.subTest(day_id=day_id):
                response = self.client.get(f"/api/traffic/day/{day_id}")
                self.assertEqual(response.status_code, 200)
    
    def test_invalid_day_ids(self):
        """Test with invalid day_id values."""
        invalid_day_ids = [0, 8]
        for day_id in invalid_day_ids:
            with self.subTest(day_id=day_id):
                response = self.client.get(f"/api/traffic/day/{day_id}")
                self.assertEqual(response.status_code, 404)

        # Test with non-integer day_id value
        response = self.client.get("/api/traffic/day/abc")
        self.assertEqual(response.status_code, 422)


if __name__ == '__main__':
    unittest.main()
