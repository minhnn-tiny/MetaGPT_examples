## test_app.py
import unittest
from unittest.mock import patch
from weather_forecast_run_tests.app import WeatherAPI, StreamlitUI, App

## <SECTION_NAME>: Mock Data
mock_current_weather_response = {
    "main": {"temp": 25, "temp_min": 22, "temp_max": 28},
    "weather": [{"main": "Clear"}],
    "wind": {"speed": 5}
}

mock_hourly_forecast_response = {
    "list": [
        {"dt_txt": "2023-04-01 09:00:00", "main": {"temp": 20}, "weather": [{"main": "Cloudy"}]},
        {"dt_txt": "2023-04-01 12:00:00", "main": {"temp": 22}, "weather": [{"main": "Sunny"}]}
    ]
}

mock_weekly_forecast_response = {
    "list": [
        {"dt_txt": "2023-04-01", "main": {"temp_max": 25, "temp_min": 18}, "weather": [{"main": "Rain"}]},
        {"dt_txt": "2023-04-02", "main": {"temp_max": 26, "temp_min": 19}, "weather": [{"main": "Clear"}]}
    ]
}

## <SECTION_NAME>: Test WeatherAPI
class TestWeatherAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.weather_api = WeatherAPI()
        self.location = "New York"

    @patch('requests.get')
    def test_get_current_weather(self, mock_get):
        mock_get.return_value.json.return_value = mock_current_weather_response
        mock_get.return_value.status_code = 200
        response = self.weather_api.get_current_weather(self.location)
        self.assertEqual(response['temp'], 25)
        self.assertEqual(response['weather'], 'Clear')
        self.assertEqual(response['wind_speed'], 5)

    @patch('requests.get')
    def test_get_hourly_forecast(self, mock_get):
        mock_get.return_value.json.return_value = mock_hourly_forecast_response
        mock_get.return_value.status_code = 200
        response = self.weather_api.get_hourly_forecast(self.location)
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0]['time'], "2023-04-01 09:00:00")
        self.assertEqual(response[0]['temp'], 20)
        self.assertEqual(response[0]['weather'], 'Cloudy')

    @patch('requests.get')
    def test_get_weekly_forecast(self, mock_get):
        mock_get.return_value.json.return_value = mock_weekly_forecast_response
        mock_get.return_value.status_code = 200
        response = self.weather_api.get_weekly_forecast(self.location)
        self.assertEqual(len(response), 2)
        self.assertEqual(response[0]['date'], "2023-04-01")
        self.assertEqual(response[0]['max_temp'], 25)
        self.assertEqual(response[0]['min_temp'], 18)
        self.assertEqual(response[0]['weather'], 'Rain')

## <SECTION_NAME>: Test StreamlitUI
class TestStreamlitUI(unittest.TestCase):
    @patch('streamlit.subheader')
    @patch('streamlit.write')
    def test_display_current_weather(self, mock_write, mock_subheader):
        ui = StreamlitUI()
        data = {"temp": 25, "weather": "Sunny", "wind_speed": 10}
        ui.display_current_weather(data)
        mock_subheader.assert_called_once_with("Current Weather")
        mock_write.assert_any_call("Temperature: 25°C")
        mock_write.assert_any_call("Weather: Sunny")
        mock_write.assert_any_call("Wind Speed: 10 km/h")

    @patch('streamlit.subheader')
    @patch('streamlit.write')
    def test_display_hourly_forecast(self, mock_write, mock_subheader):
        ui = StreamlitUI()
        data = [{"time": "09:00", "temp": 20, "weather": "Cloudy"}]
        ui.display_hourly_forecast(data)
        mock_subheader.assert_called_once_with("Hourly Forecast")
        mock_write.assert_called_once_with("Time: 09:00, Temperature: 20°C, Weather: Cloudy")

    @patch('streamlit.subheader')
    @patch('streamlit.write')
    def test_display_weekly_forecast(self, mock_write, mock_subheader):
        ui = StreamlitUI()
        data = [{"date": "2023-04-01", "max_temp": 25, "min_temp": 18, "weather": "Rain"}]
        ui.display_weekly_forecast(data)
        mock_subheader.assert_called_once_with("Weekly Forecast")
        mock_write.assert_called_once_with("Date: 2023-04-01, Max Temp: 25°C, Min Temp: 18°C, Weather: Rain")

## <SECTION_NAME>: Test App Integration
class TestAppIntegration(unittest.TestCase):
    @patch.object(StreamlitUI, 'search_bar')
    @patch.object(WeatherAPI, 'get_current_weather')
    @patch.object(WeatherAPI, 'get_hourly_forecast')
    @patch.object(WeatherAPI, 'get_weekly_forecast')
    def test_main(self, mock_weekly_forecast, mock_hourly_forecast, mock_current_weather, mock_search_bar):
        mock_search_bar.return_value = "New York"
        mock_current_weather.return_value = mock_current_weather_response
        mock_hourly_forecast.return_value = mock_hourly_forecast_response["list"][:2]
        mock_weekly_forecast.return_value = mock_weekly_forecast_response["list"][:2]
        app = App()
        app.main()
        mock_search_bar.assert_called_once()
        mock_current_weather.assert_called_once_with("New York")
        mock_hourly_forecast.assert_called_once_with("New York")
        mock_weekly_forecast.assert_called_once_with("New York")

if __name__ == '__main__':
    unittest.main()
