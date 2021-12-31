from subject import Subject


class WeatherData(Subject):
    def __init__(
            self,
            temperature: float = 0,
            humidity: float = 0,
            pressure: float = 0
    ):
        super().__init__()
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def get_temperature(self) -> float:
        return self.temperature

    def get_humidity(self) -> float:
        return self.humidity

    def get_pressure(self) -> float:
        return self.pressure

    def measurements_changed(self, new_measurements: dict) -> None:
        self.temperature = new_measurements.get(
            'temperature', self.temperature)
        self.humidity = new_measurements.get(
            'humidity', self.temperature)
        self.pressure = new_measurements.get(
            'pressure', self.temperature)

        self.notify_observers()
