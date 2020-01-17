# Python

https://docs.python.org/3/


## Coding Style
- PEP8 Guide: https://www.python.org/dev/peps/pep-0008/#package-and-module-names
- Google Style Guide: https://github.com/google/styleguide/blob/gh-pages/pyguide.md

## Favorite Resources

- quick reference: https://github.com/justmarkham/python-reference
- https://lectures.quantecon.org/py/
- https://www.pythoncheatsheet.org/
- https://treyhunner.com/
- https://www.tutorialspoint.com/python3/index.htm
- https://realpython.com/
- Data Science
    - https://datatofish.com/

## Video Tutorials
- Corey S Videos: https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7
- Google Python class: https://www.youtube.com/watch?v=tKTZoB2Vjuk&list=PLC8825D0450647509

## PIP Commands

|Shortcut | Description 
|--------|--------------------|
|pip install package |install package |
| pip install -U package| upgrade package |
|pip list | show list of installed packages |
|pip list -o /  pip list --outdated | find outdated packages |
| pip uninstall package| uninstall pkg|
| pip freeze > requirements.txt| send packages to a output file |
|pip install -r requirements.txt | use req files to install|

## Udemy Trainings
 - https://www.udemy.com/course/data-analysis-with-pandas/
    - files - https://github.com/sivabalanb/Data-Analysis-with-Pandas-and-Python 

## Generators

https://speakerd.s3.amazonaws.com/presentations/0b3d897c54204d299b25cefa92e3704a/Generators.pdf
http://www.dabeaz.com/tutorials.html
## Logging
https://docs.python.org/3/library/logging.html

Basic Usage
```
FORMAT = '%(asctime)s:%(levelname)s:%(message)s:%(module)s:%(filename)s:%(filename)s'
logging.basicConfig(filename='test.log',level=logging.INFO,format=FORMAT)
```
### Videos

-Basics: https://www.youtube.com/watch?v=-ARI4Cz-awo&t=760s
- Advanced: https://www.youtube.com/watch?v=jxmzY9soFXg
- Microsoft Tutorials: https://www.youtube.com/playlist?list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6


## GitHub Repos:
 - Microsoft: https://github.com/microsoft/c9-python-getting-started
 - Corey Shafer: https://github.com/CoreyMSchafer/code_snippets

### Guides
https://realpython.com/python-logging/#basic-configurations


## Build Tools
###  pyinstaller 
PyInstaller bundles a Python application and all its dependencies into a single package. The user can run the packaged app without installing a Python interpreter or any modules.
- download
- how to guide: https://realpython.com/pyinstaller-python/
- manual: https://pyinstaller.readthedocs.io/en/stable/index.html
- video: https://www.youtube.com/watch?v=UZX5kH72Yx4

## Flask
Flask main: https://flask.palletsprojects.com/en/1.1.x/quickstart/

Flask Cheat sheet: https://s3.us-east-2.amazonaws.com/prettyprinted/flask_cheatsheet.pdf

Videos: https://www.youtube.com/watch?v=qla-KaMF-2Q&t=945s

### Flask Code Example

```python
# jinja 2 template code to skip first and last labels on WTForms

  {% for question in form %}
          {% if loop.first or loop.last %}
            {# do not print question.label #}
          {% else %}
            <p>
              {{ question.label }}
            </p>
          {% endif %}
```
Boostrap usage:
https://github.com/mbr/flask-bootstrap

Blogs
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
## SQL Alchemy
How to Install: ```pip install flask-sqlalchemy```

sample app.py
```
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#  if first time u need to create db using db.create_all()

class Student(db.Model):
     # Manual name
	__tablename__ = 'students'
	# DDL 
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

```

Testing in command line:
```python
from app import db
db.create_all()
from app import Student

# new student
student1 = Student(first_name='anish',last_name='sebastian')
# add user 
db.session.add(student1)
# save changes
db.session.commit()

# query to get all
Student.query.all()

# get 1st result
Student.query.first()

# filter by name
Student.query.filter_by(first_name='anish').all()

# store in var
student = Student.query.first()

# get id using var
student.id

# search using id
student = Student.query.get(<id>)
```

to drop all db tables: ```db.drop_all()```

