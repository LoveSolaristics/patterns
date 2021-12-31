from observer import Observer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from weather_data import WeatherData


class CurrentConditionsDisplay(Observer):
    def __init__(
            self,
            data_source: "WeatherData",
            temperature: float = 0,
            humidity: float = 0,
            pressure: float = 0
    ):
        super().__init__()
        self.data_source = data_source
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def update(self) -> None:
        self.temperature = self.data_source.get_temperature()
        self.humidity = self.data_source.get_humidity()
        self.pressure = self.data_source.get_pressure()

    def display(self) -> str:
        return f'temperature: {self.temperature}\nhumidity: {self.humidity}' \
               f'\npressure: {self.pressure}'
