from subject import WeatherData
from display import CurrentConditionDisplay, StatisticsDisplay, ForecastDisplay

weather_data: WeatherData = WeatherData()

# register observers
condition_display: CurrentConditionDisplay = CurrentConditionDisplay(weather_data)
statistics_display: StatisticsDisplay = StatisticsDisplay(weather_data)
forecast_display: ForecastDisplay = ForecastDisplay(weather_data)


if __name__ == '__main__':
    # update measures and they would broadcast to downstream observers
    weather_data.set_measurements(23.2, 11.2, 47)
    weather_data.set_measurements(24.1, 13.2, 40)
    weather_data.set_measurements(12.1, 11.2, 60)
