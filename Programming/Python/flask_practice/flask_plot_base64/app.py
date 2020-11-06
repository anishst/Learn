# https://www.chartjs.org/

from flask import Flask, render_template
import io
import base64

app = Flask(__name__)



from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


def get_png_base64(fig):
    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return  pngImageB64String

@app.route("/", methods=["GET"])
def plotView():
    # Generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("title")
    axis.set_xlabel("x-axis")
    axis.set_ylabel("y-axis")
    axis.grid()
    x = [1,2,3,4]
    y = [45,67,56,5]
    # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.plot.html
    axis.plot(x,y, "ro-")

    # Convert plot to PNG image
    # pngImage = io.BytesIO()
    # FigureCanvas(fig).print_png(pngImage)
    #
    # # Encode PNG image to base64 string
    # pngImageB64String = "data:image/png;base64,"
    # pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    pngImageB64String = get_png_base64(fig)

    return render_template("image.html", image=pngImageB64String)

@app.route("/plot_dates", methods=["GET"])
def plot_dates():
    import datetime as dt
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    dates = ['01/02/1991', '01/03/1991', '01/04/1991']
    x = [dt.datetime.strptime(d, '%m/%d/%Y').date() for d in dates]
    y = range(len(x))  # many thanks to Kyss Tao for setting me straight here

    # Generate plot
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.plot(x, y)
    plt.gcf().autofmt_xdate()
    plt.show()

    return "helow"

@app.route("/plot_dates2", methods=["GET"])
def plot_dates2():

    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import numpy as np
    import datetime as dt

    np.random.seed(1)

    N = 100
    y = np.random.rand(N)

    now = dt.datetime.now()
    then = now + dt.timedelta(days=100)
    days = mdates.drange(now,then,dt.timedelta(days=1))

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
    plt.plot(days,y)
    plt.gcf().autofmt_xdate()
    plt.show()
    return "hellow"

if  __name__ == "__main__":
    app.run(debug=True)