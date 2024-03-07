## weather_api.py
import requests
import pandas as pd
from typing import Optional

class WeatherAPI:
    """
    WeatherAPI class to interact with the OpenWeatherMap API for fetching weather data.
    """
    def __init__(self, api_key: str):
        """
        Initializes the WeatherAPI with necessary details.
        
        :param api_key: API key for authenticating with the OpenWeatherMap API.
        """
        self.api_key: str = api_key
        self.base_url: str = "http://api.openweathermap.org/data/2.5/"

    def _get_response(self, url: str) -> Optional[dict]:
        """
        Helper method to make API requests and handle errors.
        
        :param url: The URL to fetch data from.
        :return: The JSON response as a dictionary, or None if an error occurs.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError if the response code was unsuccessful
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
        return None

    def get_current_weather(self, location: str) -> dict:
        """
        Fetches the current weather for a given location.
        
        :param location: The location for which to fetch the weather.
        :return: A dictionary containing the current weather data.
        """
        url: str = f"{self.base_url}weather?q={location}&appid={self.api_key}&units=metric"
        return self._get_response(url) or {}

    def get_hourly_forecast(self, location: str) -> list:
        """
        Fetches the hourly weather forecast for a given location.
        
        :param location: The location for which to fetch the hourly forecast.
        :return: A list of dictionaries, each containing hourly forecast data.
        """
        url: str = f"{self.base_url}forecast?q={location}&appid={self.api_key}&units=metric"
        forecast_data = self._get_response(url)
        return forecast_data.get('list', []) if forecast_data else []

    def get_weekly_forecast(self, location: str) -> list:
        """
        Fetches the weekly weather forecast for a given location, aggregating data to provide daily summaries.
        
        :param location: The location for which to fetch the weekly forecast.
        :return: A list of dictionaries, each containing daily forecast data for the week.
        """
        url: str = f"{self.base_url}forecast?q={location}&appid={self.api_key}&units=metric"
        forecast_data = self._get_response(url)
        if not forecast_data:
            return []

        # Convert forecast data to a DataFrame
        df = pd.DataFrame(forecast_data.get('list', []))
        # Extract date from 'dt_txt' and create a new column 'date'
        df['date'] = df['dt_txt'].apply(lambda x: x.split(' ')[0])
        # Aggregate data by date
        daily_summary = df.groupby('date').agg({
            'main.temp_min': 'min',
            'main.temp_max': 'max',
            'weather': lambda x: x.mode()[0][0]['main']  # Most common weather
        }).reset_index()

        # Convert DataFrame back to list of dictionaries
        return daily_summary.to_dict('records')
