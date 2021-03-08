#https://blog.heptanalytics.com/flask-plotly-dashboard/
from flask import Flask, render_template,request
import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json

app = Flask(__name__)


@app.route('/')
def index():
    feature = 'Bar'
    bar = create_plot(feature)
    return render_template('index.html', plot=bar)

@app.route('/df')
def new_plot():
    #https://pbpython.com/plotly-dash-intro.html
    # data
    df = pd.read_excel("https://github.com/chris1610/pbpython/blob/master/data/salesfunnel.xlsx?raw=True")
    # pivot table format
    pv = pd.pivot_table(df, index=['Name'], columns=["Status"], values=['Quantity'], aggfunc=sum, fill_value=0)

    # Create a trace
    data = [go.Scatter(
        x=pv.index,
        y=pv[('Quantity', 'declined')],
        mode='markers'
    )]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    # return graphJSON
    return df.to_html() + pv.to_html()

def create_plot(feature):
    if feature == 'Bar':
        N = 40
        x = np.linspace(0, 1, N)
        y = np.random.randn(N)
        df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe
        data = [
            go.Bar(
                x=df['x'], # assign x as the dataframe column 'x'
                y=df['y']
            )
        ]
    elif feature == 'Test':
        #https://pbpython.com/plotly-dash-intro.html
        df = pd.read_excel("https://github.com/chris1610/pbpython/blob/master/data/salesfunnel.xlsx?raw=True")
        # pivot table format
        pv = pd.pivot_table(df, index=['Name'], columns=["Status"], values=['Quantity'], aggfunc=sum, fill_value=0)

        # Create a trace
        data = [go.Bar(
            x=pv.index,
            y=pv[('Quantity', 'declined')]
        ),
            go.Bar(
                x=pv.index,
                y=pv[('Quantity', 'pending')]
            ),
            go.Bar(
                x=pv.index,
                y=pv[('Quantity', 'presented')]
            ),
            go.Bar(
                x=pv.index,
                y=pv[('Quantity', 'won')]
            ),
        ]
    elif feature == 'Expenses':
        #https://pbpython.com/plotly-dash-intro.html
        df = pd.read_excel("https://github.com/chris1610/pbpython/blob/master/data/salesfunnel.xlsx?raw=True")
        # pivot table format
        pv = pd.pivot_table(df, index=['Name'], columns=["Status"], values=['Quantity'], aggfunc=sum, fill_value=0)

        # Create a trace
        data = [go.Bar(
            x=pv.index,
            y=pv[('Quantity', 'declined')]
        ),
            go.Bar(
                x=pv.index,
                y=pv[('Quantity', 'pending')]
            ),
            go.Bar(
                x=pv.index,
                y=pv[('Quantity', 'presented')]
            ),
            go.Bar(
                x=pv.index,
                y=pv[('Quantity', 'won')]
            ),
        ]
    else:
        N = 1000
        random_x = np.random.randn(N)
        random_y = np.random.randn(N)

        # Create a trace
        data = [go.Scatter(
            x = random_x,
            y = random_y,
            mode = 'markers'
        )]


    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/bar', methods=['GET', 'POST'])
def change_features():

    feature = request.args['selected']
    graphJSON= create_plot(feature)

    return graphJSON

if __name__ == '__main__':
    app.run()