import numpy as np 
from flask import Flask, request, render_template, abort, Response
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)

@app.route('/')
def index():
    x = np.arange(2, 50, step=.5)
    y = np.sqrt(x) + np.random.randint(2,50)
    plot = figure(plot_width=400, plot_height=400,title=None, toolbar_location="below")
    plot.line(x,y)

    script, div = components(plot)
    kwargs = {'script': script, 'div': div}
    kwargs['title'] = 'bokeh-with-flask'    
    return render_template('index.html', **kwargs)   

if __name__ == '__main__':
    app.run(debug=True)