from flask import *
import pandas as pd



app = Flask(__name__)

@app.route("/")
def show_tables():
    pd.set_option('display.max_colwidth', -1)
    # data = pd.read_excel(r'C:\Users\532975\Documents\BAH Projects\OTCnet\Testing\Defect Screen Shots\Archives\ERROR MESSAGE TRACKER.xlsx')
    data = pd.read_excel('dummy_data.xlsx')
    return render_template('home.html',tables=[data.to_html()])

if __name__ == "__main__":
    app.run(debug=True)