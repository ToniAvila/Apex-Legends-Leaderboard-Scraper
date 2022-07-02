import datetime
from flask import Flask, render_template
import pandas as pd
import webpex
from tableExtractor import scrapedTable

app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')

# other
# @app.route('/')
# def index():
#     return render_template('index.html')

# other
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def index():
    x = webpex.allLinks()
    tablePC = scrapedTable(x[0])
    tablePS = scrapedTable(x[1])
    tableXB = scrapedTable(x[2])
    pc = tablePC.createDataFrame()
    psn = tablePS.createDataFrame()
    xbox = tableXB.createDataFrame()
    today = datetime.date.today()


    return render_template("index.html", 
                            dataPC=pc.to_html(classes='table table-stripped'),
                            dataPSN=psn.to_html(classes='table table-stripped'),
                            dataXB=xbox.to_html(classes='table table-stripped'),
                            date=today.strftime('%d, %b %Y'))

if __name__ == "__main__":
    app.run(debug=True)