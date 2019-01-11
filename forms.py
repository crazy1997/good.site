from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class WeatherForm(FlaskForm):
	city_name   = StringField("Enter your city!" )
	submit = SubmitField("Submit")

class MovieForm(FlaskForm):
	movie_name   = StringField("Вводите свою дату")
	movie_submit = StringField("Submit")