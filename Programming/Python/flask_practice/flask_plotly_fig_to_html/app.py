import datetime

from flask import Flask, render_template
app = Flask(__name__)
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import yfinance as yf




@app.route('/')
def chart():
    # return  "Hello"
    # https://plotly.com/python/time-series/
    df = px.data.stocks()
    fig = px.line(df, x="date", y=df.columns,
                  hover_data={"date": "|%B %d, %Y"},
                  title='custom tick labels')
    fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y")
    data = fig.to_html(full_html=False)

    df = px.data.tips()
    fig = px.box(df, x="day", y="total_bill", color="smoker", notched=True)
    data2 = fig.to_html(full_html=False)

    # get historical data
    start = datetime.datetime(2021, 3, 1)
    end = datetime.datetime.now()

    tickerSymbols = ["VOO", "MSFT", "ARKK", "VTI", "BAH", "VFINX"]

    first_ticker = True
    for ticker in tickerSymbols:
        tickerData = yf.Ticker(ticker)
        tickerDf = tickerData.history(period='1d', start=start, end=end)
        # add stock symbol as a column value
        tickerDf.insert(0, "stock", ticker)
        if first_ticker:
            tickerDf.to_csv("data/mystocks.csv", mode='w')
            first_ticker = False
        else:
            # append and skip headers after first item
            tickerDf.to_csv("data/mystocks.csv", mode='a', header=False)
    tbl = pd.read_csv('data/mystocks.csv', index_col=0, parse_dates=True).to_html()

    # https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.to_html
    return  render_template('index.html', data=data, data2=data2, tbl=tbl)

if __name__ == '__main__':
    app.run(debug=True)