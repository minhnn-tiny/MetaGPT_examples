## app.py
import streamlit as st
import requests

class StreamlitUI:
    def display_current_weather(self, data: dict):
        st.subheader("Current Weather")
        st.write(f"Temperature: {data['temp']}°C")
        st.write(f"Weather: {data['weather']}")
        st.write(f"Wind Speed: {data['wind_speed']} km/h")

    def display_hourly_forecast(self, data: list):
        st.subheader("Hourly Forecast")
        for hour in data:
            st.write(f"Time: {hour['time']}, Temperature: {hour['temp']}°C, Weather: {hour['weather']}")

    def display_weekly_forecast(self, data: list):
        st.subheader("Weekly Forecast")
        for day in data:
            st.write(f"Date: {day['date']}, Max Temp: {day['max_temp']}°C, Min Temp: {day['min_temp']}°C, Weather: {day['weather']}")

    def search_bar(self) -> str:
        return st.text_input("Enter location", "New York")

class WeatherAPI:
    api_key: str = "f9ee5b45c99d86649d7047c837c15096"  # Set your OpenWeatherMap API key here
    base_url: str = "http://api.openweathermap.org/data/2.5/"

    def handle_api_response(self, response):
        if response.status_code == 401:
            st.error("Invalid API key. Please check your API key.")
            return None
        elif response.status_code == 404:
            st.error("Location not found. Please enter a valid location.")
            return None
        elif response.status_code != 200:
            st.error("Failed to fetch data. Please try again later.")
            return None
        return response.json()

    def get_current_weather(self, location: str) -> dict:
        response = requests.get(f"{self.base_url}weather?q={location}&appid={self.api_key}&units=metric")
        data = self.handle_api_response(response)
        if data is None:
            return {}
        return {
            "temp": data["main"]["temp"],
            "weather": data["weather"][0]["main"],
            "wind_speed": data["wind"]["speed"]
        }

    def get_hourly_forecast(self, location: str) -> list:
        response = requests.get(f"{self.base_url}forecast?q={location}&appid={self.api_key}&units=metric")
        data = self.handle_api_response(response)
        if data is None:
            return []
        forecast = []
        for item in data["list"][:8]:  # Get the next 8 hours forecast
            forecast.append({
                "time": item["dt_txt"],
                "temp": item["main"]["temp"],
                "weather": item["weather"][0]["main"]
            })
        return forecast

    def get_weekly_forecast(self, location: str) -> list:
        response = requests.get(f"{self.base_url}forecast?q={location}&appid={self.api_key}&units=metric")
        data = self.handle_api_response(response)
        if data is None:
            return []
        forecast = []
        # Simplified example of aggregating data for a weekly forecast
        for item in data["list"][:7]:  # Assuming the first 7 items as a week's forecast
            forecast.append({
                "date": item["dt_txt"].split(" ")[0],  # Extracting date
                "max_temp": item["main"]["temp_max"],
                "min_temp": item["main"]["temp_min"],
                "weather": item["weather"][0]["main"]
            })
        return forecast

class App:
    def __init__(self):
        self.ui = StreamlitUI()
        self.weather_api = WeatherAPI()

    def main(self):
        location = self.ui.search_bar()
        current_weather_data = self.weather_api.get_current_weather(location)
        if current_weather_data:
            self.ui.display_current_weather(current_weather_data)
        hourly_forecast_data = self.weather_api.get_hourly_forecast(location)
        if hourly_forecast_data:
            self.ui.display_hourly_forecast(hourly_forecast_data)
        weekly_forecast_data = self.weather_api.get_weekly_forecast(location)
        if weekly_forecast_data:
            self.ui.display_weekly_forecast(weekly_forecast_data)

if __name__ == "__main__":
    app = App()
    app.main()
