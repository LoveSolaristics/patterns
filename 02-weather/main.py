from weather_data import WeatherData
from display import CurrentConditionsDisplay

if __name__ == "__main__":
    data = WeatherData()

    display_1 = CurrentConditionsDisplay(data)
    data.register_observer(display_1)
    print('Начальные значения:', display_1.display(), sep='\n')

    data.measurements_changed({"temperature": 10,
                               "humidity": 5,
                               "pressure": 15})
    print('\nОбновленные значения:', display_1.display(), sep='\n')

