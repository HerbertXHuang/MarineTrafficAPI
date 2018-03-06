from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
	r = requests.get('https://api.icndb.com/jokes/random')
	data = json.loads(r.text)
	joke = data['value']['joke']

	return render_template('index.html', joke = joke)
