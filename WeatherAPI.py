import pyowm 


owm = pyowm.OWM('c1883ba9de7d50cbb87f992c64eb209f', language = 'ru')

city_name = 'London'

observation = owm.weather_at_place(city_name)
w = observation.get_weather()
a = w.get_detailed_status()


print(w,a,w.get_wind())