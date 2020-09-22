import pyowm
#from pyowm.utils import timestamps
import datetime


api_key = "22e8fcc922b5c64d361c979d1829079a"
owm = pyowm.OWM(api_key)
mgr = owm.weather_manager()

three_hour_forecaster = mgr.forecast_at_place('Berlin,DE', '3h')
start_date = datetime.date.today()
for i in range(1,5): # Range chosen based on what program allowed
    for j in range(0,24,3):
        #date = start_date + datetime.timedelta(days=i,hours=j)
        date = datetime.datetime(start_date.year, start_date.month, start_date.day+i, j, 0, 0)
        #date = datetime.datetime(2020, 9, 22+i, j, 0, 0)
        weather = three_hour_forecaster.get_weather_at(date)
        print(weather.temperature('fahrenheit')['temp'])
        print(date,i)



#datetime.datetime(2020, 9, 23, 0, 0, 0).isoformat()
#datetime.datetime(2020, 9, 23, 3, 0, 0).isoformat()



'''
now = datetime.datetime.now()
Sept_21 = now - datetime.timedelta(days=1)
Sept_20 = now - datetime.timedelta(days=2)
Sept_19 = now - datetime.timedelta(days=3)
new = timestamps.tomorrow(Sept_20)
three_hour_forecaster = mgr.forecast_at_place('Berlin,DE', '3h')
weather = three_hour_forecaster.get_weather_at(Sept_20)
print(weather)
'''



#for i in range(0,7):
#	day = datetime.datetime.today() + datetime.timedelta(days=i)





'''
three_hour_forecaster = mgr.forecast_at_place('Berlin,DE', '3h')
tomorrow_at_five = timestamps.tomorrow(2, 0)                      # datetime object for tomorrow at 5 PM
tomorrow_at_eight = timestamps.tomorrow(20, 0)
weather_5 = three_hour_forecaster.get_weather_at(tomorrow_at_five)   
weather_8 = three_hour_forecaster.get_weather_at(tomorrow_at_eight)
print(weather_5)
'''

#print(weather_5.temperature('fahrenheit')['temp'])
#print(weather_8.temperature('fahrenheit')['temp'])







'''
import requests
import json
city_name = "London"
state_code = "uk"

url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code}&appid={api_key}'
r = requests.get(url)

j=r.json()
print(j)
'''

cincinnati_id = 4508722

'''
reg = owm.city_id_registry()
list_of_tuples = reg.ids_for('cincinnati', country='OH', matching='like') 
print(list_of_tuples)
'''

#daily_forecast = mgr.forecast_at_place('Berlin,DE', 'daily').forecast


'''
one_call = mgr.one_call(lat=52.5244, lon=13.4105)
print(one_call.forecast_hourly[0].reference_time)
print(one_call.forecast_hourly[0].temperature('fahrenheit')['temp'])
'''

'''
three_hour_forecaster = mgr.forecast_at_place('Berlin,DE', '3h')
tomorrow_at_five = timestamps.tomorrow(17, 0)                      # datetime object for tomorrow at 5 PM
tomorrow_at_eight = timestamps.tomorrow(20, 0)    
weather_5 = three_hour_forecaster.get_weather_at(tomorrow_at_five)   
weather_8 = three_hour_forecaster.get_weather_at(tomorrow_at_eight)
print(weather_5.temperature('fahrenheit')['temp'])
print(weather_8.temperature('fahrenheit')['temp'])
'''

'''three_hr_forecast = mgr.forecast_at_place('Berlin,DE', '3h').forecast
print(three_hr_forecast)
for weather in three_hr_forecast:
	print(weather.reference_time)

	break
	'''

    #print(weather.get_reference_time('iso'), weather.get_status())
'''
historian = mgr.station_hour_history(39276)
print(len(historian))
print(historian)
'''

'''
observation = mgr.weather_at_place('London,uk')
weather = observation.weather
temp_dict_fahrenheit = weather.temperature('fahrenheit')
print(len(temp_dict_fahrenheit))
print(temp_dict_fahrenheit)
'''
#print(weather.status) # short version of status (eg. 'Rain')
#print(weather.detailed_status)



#w = observation.get_weather()
#print(w)



#w.get_wind()
#{u'speed': 3.1, u'deg': 220}
#w.get_humidity()