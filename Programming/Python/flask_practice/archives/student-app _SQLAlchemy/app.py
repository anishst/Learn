# https://www.youtube.com/watch?v=LPdWU9VF-Po&t=1659s
# https://www.youtube.com/watch?v=e3S9yYKV97E
from flask import Flask, request, redirect, url_for,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

modus = Modus(app)
db = SQLAlchemy(app)

#  if first time u need to create db using db.create_all()

class Student(db.Model):

	__tablename__ = 'students'

	# DDL 
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	# magic method; how our object is going to be printed
	def __repr__(self):
		return f"Student('{self.first_name}','{self.last_name}')"

@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/students', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		new_student = Student(request.form['first_name'], request.form['last_name'])
		db.session.add(new_student)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('index.html', students=Student.query.all())

@app.route('/students/new')
def new():
	return render_template('new.html')

@app.route('/students/<int:id>', methods=['GET','PATCH', 'DELETE'] )
def show(id):
	found_student = Student.query.get(id)
	if request.method == b'PATCH':
		found_student.first_name = request.form['first_name']
		found_student.last_name = request.form['last_name']
		db.session.add(found_student)
		db.session.commit()
		return redirect(url_for('index'))
	if request.method == b'DELETE':
		db.session.delete(found_student)
		db.session.commit()
		return redirect(url_for('index'))

	return render_template('show.html', student=found_student)


@app.route('/students/<int:id>/edit')
def edit(id):
	found_student = Student.query.get(id)
	return render_template('edit.html', student=found_student)

import webbrowser
webbrowser.open("http://localhost:5000")

if __name__ == '__main__':
	app.run(debug=True)