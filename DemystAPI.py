from flask import Flask, request, render_template, url_for, redirect
from static.MarineTraffic import MarineTraffic

app = Flask(__name__)

# Make the output more human-friendly
def prettify(array):
	string = list(map(lambda x:  '; '.join(x[0]) + '<br>' + '<br>'.join(x[1]), array))		
	for i in range(len(string)):
		string[i] = 'No.' + str(i+1)+ ': ' + string[i]
	return '<br><br>'.join(string)

@app.route('/', methods = ['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	if request.method == 'POST':
		keyword = request.form['keyword']
		return redirect(url_for('search_page', keyword = keyword))

@app.route('/query', methods = ['GET', 'POST'])
def search_page():
	keyword = request.args.get('keyword')
	sum_res, res = MarineTraffic().Search(keyword)
	if len(res)>0:
		res = prettify(res)
	if request.method == 'GET':
		return render_template('index.html', sum_res = sum_res, result = res)
	if request.method == 'POST':
		keyword = request.form['keyword']
		return redirect(url_for('search_page', keyword = keyword))

# Do not use app.run() for deployment, error might occur otherwise