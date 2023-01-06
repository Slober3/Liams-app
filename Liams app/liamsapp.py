from flask import Flask, render_template,request, redirect
from flask_bootstrap import Bootstrap
import csv

app = Flask(__name__)
Bootstrap(app)

@app.route('/submit', methods=['GET'])
def submit():
    score = request.args['score']
    name = request.args['name']

    with open('scores.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, score])
        csvfile.close()
    return redirect('/')

@app.route('/')
def scores():
    rows = []
    with open('scores.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
    return render_template('scores.html', rows=rows)