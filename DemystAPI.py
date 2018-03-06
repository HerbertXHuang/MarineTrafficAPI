from flask import Flask, request, render_template
from static.MarineTraffic import MarineTraffic

app = Flask(__name__)

def prettify(array):
	string = list(map(lambda x:  '; '.join(x[0]) + '<br>' + '<br>'.join(x[1]), array))		
	for i in range(len(string)):
		string[i] = 'NO.' + str(i+1)+ ': ' + string[i]
	return '<br>'.join(string)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
    	return render_template('index.html')

    if request.method == 'POST':
    	keyword = request.form['keyword']
    	sum_res, res = MarineTraffic().Search(keyword)
    	if len(res)>0:
	    	res = prettify(res)
    	return render_template('index.html', sum_res = sum_res, result = res)
