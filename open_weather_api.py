import pyowm
import datetime

api_key = "22e8fcc922b5c64d361c979d1829079a"

class DataSource:

    def read(self, **kwargs):
        temperatures_by_hour = {}
        #url = kwargs['url']
        owm = pyowm.OWM(api_key)
        mgr = owm.weather_manager()

        three_hour_forecaster = mgr.forecast_at_place('Berlin,DE', '3h')
        start_date = datetime.date.today()
        for i in range(1,5): # Range chosen based on what program allowed
            for j in range(0,24,3):
                date = datetime.datetime(start_date.year, start_date.month, start_date.day+i, j, 0, 0)
                weather = three_hour_forecaster.get_weather_at(date)
                temperatures_by_hour[date.isoformat()] = weather.temperature('fahrenheit')['temp']

        return temperatures_by_hour