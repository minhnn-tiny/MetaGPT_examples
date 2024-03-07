## test_weather_api.py
import unittest
from unittest.mock import patch
from weather_forecast_run_tests.weather_api import WeatherAPI

class TestWeatherAPI(unittest.TestCase):
    """
    Test cases for the WeatherAPI class.
    """

    ## SETUP
    def setUp(self) -> None:
        """
        Set up test case environment.
        """
        self.api_key: str = "test_api_key"
        self.weather_api = WeatherAPI(api_key=self.api_key)
        self.location: str = "London"
        self.base_url: str = "http://api.openweathermap.org/data/2.5/"

    ## TEST _get_response METHOD
    @patch("weather_forecast_run_tests.weather_api.requests.get")
    def test_get_response_success(self, mock_get):
        """
        Test _get_response method returns correct data on success.
        """
        mock_get.return_value.json.return_value = {"data": "success"}
        mock_get.return_value.raise_for_status = lambda: None  # Simulate no exceptions
        url = f"{self.base_url}weather?q={self.location}&appid={self.api_key}&units=metric"
        response = self.weather_api._get_response(url)
        self.assertEqual(response, {"data": "success"})

    @patch("weather_forecast_run_tests.weather_api.requests.get")
    def test_get_response_http_error(self, mock_get):
        """
        Test _get_response method handles HTTP errors correctly.
        """
        mock_get.side_effect = Exception("HTTP Error")
        url = f"{self.base_url}weather?q={self.location}&appid={self.api_key}&units=metric"
        response = self.weather_api._get_response(url)
        self.assertIsNone(response)

    ## TEST get_current_weather METHOD
    @patch("weather_forecast_run_tests.weather_api.WeatherAPI._get_response")
    def test_get_current_weather(self, mock_get_response):
        """
        Test get_current_weather method returns correct data.
        """
        mock_get_response.return_value = {"weather": "sunny"}
        response = self.weather_api.get_current_weather(self.location)
        self.assertEqual(response, {"weather": "sunny"})

    ## TEST get_hourly_forecast METHOD
    @patch("weather_forecast_run_tests.weather_api.WeatherAPI._get_response")
    def test_get_hourly_forecast(self, mock_get_response):
        """
        Test get_hourly_forecast method returns correct data.
        """
        mock_get_response.return_value = {"list": [{"hourly": "data"}]}
        response = self.weather_api.get_hourly_forecast(self.location)
        self.assertEqual(response, [{"hourly": "data"}])

    ## TEST get_weekly_forecast METHOD
    @patch("weather_forecast_run_tests.weather_api.WeatherAPI._get_response")
    def test_get_weekly_forecast(self, mock_get_response):
        """
        Test get_weekly_forecast method returns correct aggregated data.
        """
        mock_get_response.return_value = {
            "list": [
                {
                    "dt_txt": "2023-04-01 12:00:00",
                    "main": {"temp_min": 10, "temp_max": 15},
                    "weather": [{"main": "Clouds"}]
                },
                {
                    "dt_txt": "2023-04-01 15:00:00",
                    "main": {"temp_min": 11, "temp_max": 16},
                    "weather": [{"main": "Rain"}]
                }
            ]
        }
        response = self.weather_api.get_weekly_forecast(self.location)
        self.assertIsInstance(response, list)
        self.assertGreater(len(response), 0)
        self.assertIn("date", response[0])
        self.assertIn("main.temp_min", response[0])
        self.assertIn("main.temp_max", response[0])
        self.assertIn("weather", response[0])

if __name__ == "__main__":
    unittest.main()
