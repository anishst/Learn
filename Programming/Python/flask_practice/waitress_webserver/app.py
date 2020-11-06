# https://medium.com/better-programming/introduction-to-waitress-a-wsgi-server-for-python-2-and-3-c77e20cb292b
# https://docs.pylonsproject.org/projects/waitress/en/stable/
from waitress import serve
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'

if __name__ == "__main__":
    # serve(app)  # default port 8080
    serve(app, host='0.0.0.0', port=5000)