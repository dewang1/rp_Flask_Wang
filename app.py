from flask import Flask, render_template, url_for, request, jsonify
from datetime import datetime
import pyrebase

app = Flask(__name__)
config = {}
key = 0

@app.route("/")                                     # Landing Page
def index():
    return render_template("index.html")

@app.route("/authors")                              # Authors Page
def authors():
    return render_template("authors.html")

@app.route("/procedures")                           # Procedures Page
def procedures():
    return render_template("procedures.html")

@app.route("/results")                              # Results Page
def results():
    return render_template("results.html")

@app.route('/data')                                 # Get Data
def data():
    with open('static/data/meanInhibitionZones.csv') as f:
        return f.read()
    
# Run server on local IP address at port 5000
if(__name__ == "__main__"):
    app.run(debug=False, host='10.119.11.135', port=5000)