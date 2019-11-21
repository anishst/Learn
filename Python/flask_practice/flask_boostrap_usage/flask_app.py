# https://www.youtube.com/watch?v=PE9ZGniSDW8&list=PLXmMXHVSvS-ABlT4k4eS3YPJSnPUozw04&index=8

from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)

