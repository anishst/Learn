# https://wtforms.readthedocs.io/en/stable/index.html
from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.validators import InputRequired
from wtforms.fields.html5  import DateField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'

class LoginForm(Form):
	username = StringField('username', validators=[InputRequired()])
	password = PasswordField('password')
	dt = DateField('DatePicker', format='%Y-%m-%d')


@app.route("/", methods=['GET', 'POST'])
def index():
	form = LoginForm()
	if form.validate_on_submit():
		return "Form submitted"
	return render_template("index.html", form=form)

if __name__ == '__main__':
	app.run(debug=True)