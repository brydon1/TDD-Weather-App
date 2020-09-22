import datetime
from open_weather_api import DataSource

def test_read():
    reader = DataSource()
    for key, value in reader.read(url='').items():
        assert datetime.datetime.fromisoformat(key)
        assert value - 0 == value
