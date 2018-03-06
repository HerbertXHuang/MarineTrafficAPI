from flask import Flask, render_template
import json
from static.MarineTraffic import MarineTraffic

"""
app = Flask(__name__)

@app.route('/')
def index():
    
    res = MarineTraffic().Search('YING XIANG')

    return render_template('index.html', joke = res)
"""

res = MarineTraffic().Search('YING XIANG')
print(res)