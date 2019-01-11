from flask import Flask, render_template, request
from forms import WeatherForm, MovieForm
import pyowm 

owm = pyowm.OWM('c1883ba9de7d50cbb87f992c64eb209f', language = 'ru')



app  =  Flask(__name__)
app.debug  =  True
app.config['SECRET_KEY'] = 'mysite is protected'


@app.route('/')
def main():
	return render_template('index.html')



@app.route('/courses')	
def courses1():
	return render_template('courses.html')



@app.route('/movies', methods = ['GET', 'POST'])
def movies1():
	movie_name = False
	form       = MovieForm()

	if form.validate_on_submit():
		movie_name = form.movie_name.data
		form.movie_name.data = ''
	return render_template('movies.html', movie_name = movie_name, form = form,)



@app.route('/weather', methods= ['GET', 'POST'] )
def weather1():
#погода на минск на сегодня и на 3 часа

	observation = owm.weather_at_place('Минск')
	w = observation.get_weather()
	minsk_time = w.get_reference_time(timeformat = 'iso')
	minsk_temp = w.get_temperature('celsius')['temp']
	minsk_cloud = w.get_detailed_status()

# form of weather app
	city_name = False
	form = WeatherForm()

	if form.validate_on_submit():
		city_name = form.city_name.data
		form.city_name.data = ''

	return render_template('weather.html', 
		form = form, 
		city_name = city_name, 
		minsk_time = minsk_time,
		minsk_temp = minsk_temp,
		minsk_cloud = minsk_cloud
		)			




if __name__ == '__main__':
		app.run()	