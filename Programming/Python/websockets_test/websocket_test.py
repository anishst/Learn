# https://medium.com/koko-networks/using-websockets-with-python-4396e54d36e6

from flask import Flask, render_template
from flask_socketio import SocketIO

# Initializing the flask object
app = Flask(__name__)

#  Initializing the flask-websocketio
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# If you are running it using python <filename> then below command will be used
if __name__ == '__main__':
    socketio.run(app)