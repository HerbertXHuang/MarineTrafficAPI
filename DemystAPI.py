from flask import Flask, render_template
import json
from static.MarineTraffic import MarineTraffic


app = Flask(__name__)

@app.route('/')
def index():
    
    res = MarineTraffic().Search('YING XIANG HONG')

    return render_template('index.html', joke = res)
