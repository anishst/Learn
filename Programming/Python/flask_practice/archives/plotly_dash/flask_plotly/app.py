# https://code.tutsplus.com/tutorials/charting-using-plotly-in-python--cms-30286
from flask import Flask, render_template
import json
from chart_studio.plotly import plot, iplot
import plotly.graph_objs as go



 
import numpy as np
 
app = Flask(__name__)
 
@app.route('/showLineChart')
def line():
    count = 500
    xScale = np.linspace(0, 100, count)
    yScale = np.random.randn(count)
 
    # Create a trace
    trace = go.Scatter(
        x = xScale,
        y = yScale
    )
 
    data = [trace]
    graphJSON = json.dumps(data, cls=utils.PlotlyJSONEncoder)
    return render_template('chart.html',
                               graphJSON=graphJSON)


if __name__ == "__main__":
    app.run(debug=True)