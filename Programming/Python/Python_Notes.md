# Python

- [Documentation/Resource](#docs)
- [PIPENV](#pipenv)

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

## Code snippets

### shows where python is installed
```python
import sys
sys.executable
```
### Combine nested for loops
```python

from itertools import product

list1 = range(1,3)
list2 = range(4,6)
list3 = range(7,9)

for l1, l2, l3 in product(list1,list2, list3):
    print(l1+l2+l3)
```
### itertools-library

https://medium.com/fintechexplained/advanced-python-itertools-library-the-gem-of-python-language-99da37dfcca2

### Enum

https://medium.com/better-programming/enumerations-in-python-b01a1fb479de

## Useful Python Commands

|Shortcut | Description 
|--------|--------------------|
|python -m site |shows path locations |

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

## Package Manager

### <a name="pipenv"></a>PIPENV
Python package dependency management tool.

|Command|	Description|
|------|-----|
pip install pipenv|installs pipenv
|pipenv install <packagename>|creates a new VENV; creates 2 files: Pipfile and Pipfile.lock (shouldn't modify this)|
|pipenv install -r <requirements.txt>|Install from req file|
|pipenv lock -r|show dependecies:|
|pipenv install <packagename> --dev| Install this package in only in dev env|
|pipenv uninstall <packagename>|Removing a package|
|pipenv shell|activate VENV|
pipevn check|checks for issues with packages
|pipenv -venv|get path to the VM|
|pipenv instll|install packages using the pipfile|
|pipenv --where|shows where my project is|
|pipenv --rm|remove a VM|
|pipenv graph|shows a graph of dependcies|
|pipenv lock|get ready for lock|

**Docs**:

- https://pipenv.readthedocs.io/en/latest/
- https://realpython.com/pipenv-guide/

## Data Classes

```python
from dataclasses import dataclass

@dataclass
class Coordinate:
    x: int
    y: int
    z: int
```
- @dataclass decorator is used to create a data class. x, y and z are fields in our data class. 
- By default, data classes come with __init__, __repr__ and __eq__ methods implemented so you don’t have to implement these methods by yourself.
- By default, data classes are mutable which means you can assign value to your fields. 
- Resources:
    - https://towardsdatascience.com/data-classes-in-python-8d1a09c1294b
    
    
**Video Tutorials**:
- Corey - https://www.youtube.com/watch?v=zDYL22QNiWk
- Pretty Printed - https://www.youtube.com/watch?v=tRmmjlVHzno

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

## Mock Tests

Mocking is the practice of replacing real objects with mocked objects, which mimic their behavior, at runtime. So, instead of a sending a real HTTP request over the network, we just return an expected response when the mocked method is called.

Examples:
  - https://testdriven.io/blog/testing-python/
  - [pytest monkeypatch info](https://docs.pytest.org/en/stable/monkeypatch.html)
## Regular Expressions

- . (dot) - any char
- \w - word char; includes alpha chars and digits; space is not word char
- \d - one digit
- \d? Zeor or one digits
- \d* Zeor or more digits
- \d+ one more digits
- \d{3} exactly 3 digits
- \d{3,5} btwn 3 and 5 digits
- \d{3,} 3 or more digits
- \s  whitespace
- \+ plus to the right of something means one or more
- .+ - period plus goes all the way to end
- 0 - zero to the right of something means zero or more

User square brackets to build the character set:
Example:```[\w.]+@[\w.]+ ```

- this finds email in the format of anish.sebastian@gmail.com

Use parantheses to group results:
```python
m = re.search(r'([\w.]+)@([\w.]+)', "blah nick.p@gmail.com")```
print(m.group(0))
print(m.group(1)) # get username; 1 refers to 1st paranetheses
print(m.group(2)) # get domain
```

 

### Python Regular Expression Engine

**re.match** - searches from left to right; stops as soon as first match is found

**re.findall** - finds all matches and returns the matches in a list. If parantheses are used, items will be in tuples in the list

**rawstring** - do not do any processing.
ex. r"[a-zA-Z]+ \d{1}"

### Regex practice


- https://regex101.com/
- http://www.pyregex.com/
- http://regexr.com
- https://www.browserling.com/tools/text-from-regex

## Python Videos

-Basics: https://www.youtube.com/watch?v=-ARI4Cz-awo&t=760s
- Advanced: https://www.youtube.com/watch?v=jxmzY9soFXg
- Microsoft Tutorials: https://www.youtube.com/playlist?list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6


## GitHub Repos:
 - Microsoft: https://github.com/microsoft/c9-python-getting-started
 - Corey Shafer: https://github.com/CoreyMSchafer/code_snippets

### Guides
https://realpython.com/python-logging/#basic-configurations

## GUI Frameworks

Top 10: https://towardsdatascience.com/top-10-python-gui-frameworks-for-developers-adca32fbe6fc

###TKInter
- https://docs.python.org/3.6/library/tk.html
- https://wiki.python.org/moin/TkInter

### PyQt
- https://riverbankcomputing.com/software/pyqt/intro
- https://wiki.python.org/moin/PyQt
- http://doc.qt.io/

### kivy
- https://kivy.org/#home
- good for mobile/games
- looks different than typical application

### BeeWare
- https://pybee.org/
- new

### PyGame
- https://www.pygame.org/news

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



## My Favorite Python Libraries

- Pillow - image manipulation lib
- cx-Oracle (6.2.1) - for working with oracle databases
- numpy (1.14.1) - data analysis
- pandas (0.22.0) - data analysis
- pip (9.0.1) - package install
- selenium (3.10.0)- web automation
- Selenium with Python
- XlsxWriter (1.0.2)- working with excel package
- virtualenv - for virtual environments
- pyperclip - for copying text to clipboar
- pipenv
- requests-html - for web scraping

## Python on Linux

Most linux version (Ubuntu, ElemOS) come pre-installed with python 2.7 and 3.5 version. to access 3.5 use
python3
command; to use python 3 version of packages use
pip3 install <package name>

```bash
# Ubuntu 18.04, Ubuntu 20.04 and above
sudo apt-get update
sudo apt-get install python3.8 python3-pip

# Linux Mint and Ubuntu 17 and below:
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.8 python3-pip
```

Install pip 
apt install python3-pip
sudo pip install Flask

https://realpython.com/installing-python/

## GUI Dev Options

- tkinter
- PyQt
    - qt designer https://build-system.fman.io/qt-designer-download
    - qt : https://www.qt.io/offline-installers
    
    
## Python Deployement Tools

- pyinstaller - https://www.pyinstaller.org/
- Breifcase: https://beeware.org/project/projects/tools/briefcase/
- https://pyoxidizer.readthedocs.io/en/stable/

## <a name="docs"></a>Documentation

Official Documentation
- Google Style Guide: https://github.com/google/styleguide/blob/gh-pages/pyguide.md

Python Tutorials:
- https://www.tutorialspoint.com/python3/python_cgi_programming.htm
- https://realpython.com/
- Google Python class: https://www.youtube.com/watch?v=tKTZoB2Vjuk&list=PLC8825D0450647509
- http://introtopython.org/
- Python Tips: http://book.pythontips.com/en/latest/index.html
- Cheat sheet: https://www.pythoncheatsheet.org/

### Video Tutorials
- Corey S Videos: https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7
- Google Python class: https://www.youtube.com/watch?v=tKTZoB2Vjuk&list=PLC8825D0450647509
- MIT - https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00-introduction-to-computer-science-and-programming-fall-2008/video-lectures/


