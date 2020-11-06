from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = '2323FDDF4$$@@#@3'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_background/<mode>')
def set_background(mode):
   session['mode'] = mode
   return redirect(url_for('index'))

@app.route('/drop_session')
def drop_session():
    # drop session value
    session.pop('mode', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)