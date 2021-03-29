# https://stackoverflow.com/questions/50120694/get-individual-graphs-from-plotly-using-flask-and-python
from flask import Flask, render_template,request
import plotly
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
import json

app = Flask(__name__)


@app.route('/')
def index():
    # 1st grapsh
    # Create a trace
    graph1 = [go.Scatter(
        x=[1,2,3,4],
        y=[1,2,3,4],
        mode='markers'
    )]


    graph2 = [go.Scatter(
        x=[1,2,3,4],
        y=[1,2,3,4],
        mode='markers'
    )]
    # 2n graph

    graphs = [
        dict(
            data=[graph1, graph2],
            layout=dict(
                title='Brain Data'
            )
        ),
        dict(
            data=[graph1, graph2],
            layout=dict(
                title='Accelerometer Data'
            )
        ),
    ]

    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', title='Home', ids=ids, graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)