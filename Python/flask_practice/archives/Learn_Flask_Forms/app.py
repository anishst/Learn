from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, RadioField, 
					BooleanField, DateTimeField, DateField, 
					SelectField, TextField, TextAreaField)

from wtforms.validators import DataRequired


app = Flask(__name__)


app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

	breed = StringField('What Breed are you?', validators=[DataRequired()])
	neutered = BooleanField("Have you been neutered?")
	# radio field; tuple pair
	mood = RadioField("Please choose your moood:", 
						choices=[('moode_one', "Happy"),('moode_two', "Excited") ])
	food_choice = SelectField(u"Pick your favorite food:",
						choices=[('chi', 'Chicken'), ('bf', 'Beef'), ('fish', "Fish")])
	feedback = TextAreaField()
	submit = SubmitField("Submit")


@app.route("/", methods=['GET', 'POST'])
def index():
	form = InfoForm()

	if form.validate_on_submit():
		flash("Form submitted!")

		#  store values in session object; a temp dir on server
		session['breed'] = form.breed.data
		session['neutered'] = form.neutered.data
		session['mood'] = form.mood.data
		session['food'] = form.food_choice.data
		session['feedback'] = form.feedback.data

		return redirect(url_for('thankyou'))

	return render_template('index.html', form=form)


@app.route("/thankyou")
def thankyou():
	return render_template('thankyou.html')


if __name__ == '__main__':
	app.run(debug=True)
