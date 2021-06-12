from flask import Flask
import os, sys
import platform


app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello world! from {sys.version} {platform.release()} {platform.system()}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)