import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir)

#  Setup DB
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Setup model

class Task_Model(db.Model):

	# manual table name
	__tablename__ = 'tasks_2'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text)
	description = db.Column(db.Text)
	due_date = db.Column(db.DateTime)

	# setup init method

	def __init__(self, title, description, due_date):
		self.title = title
		self.description = description
		self.due_date = due_date

	#  string representation
	def __repr__(self):
		return f"Task Details: { self.id} {self.title} {self.description} {self.due_date}"







