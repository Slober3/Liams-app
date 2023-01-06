from flask import Flask, render_template,request, redirect
from flask_bootstrap import Bootstrap
import csv
import pandas as pd

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
    dataFrame = pd.read_csv("scores.csv")
    dataFrame.sort_values(["score"],axis=0, ascending=False,inplace=True,na_position='first')

  #  with open('scores.csv', 'r') as csvfile:
   #     reader = csv.reader(csvfile)
    #    data = sorted(reader, key=operator.itemgetter(1), reverse=True)    
     #   for row in data:
      #      rows.append(row)

    return render_template('scores.html', tables=[dataFrame.to_html(classes="table table-striped",index=False).replace('border="1"','border="0"').replace('<tr style="text-align: right;">', '<tr>')], titles=[''])