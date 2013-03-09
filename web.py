#!/usr/bin/python

from flask import *

import os

import sqlite3 

app = Flask(__name__)

def home():
  return render_template('home.html')


@app.route('/raw')

def raw():
  return open('temp.data').read()       

@app.route('/')
@app.route('/temp')
def temp():
  graphdata = []
  con = get_dbhandle()
  cur = con.cursor()
  cur.execute('select timestamp, insidetemp_f, outsidetemp_f from trends')
  while True:
    row = cur.fetchone()
    if row == None:
       break

    graphdata.append("['%s', %s, %s]" % (row[0], row[1], row[2])) 



  displaydata = "[['Date','Inside','Outside']," + ",".join(graphdata) + "]" 

  data = """
<html>
  <head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
 google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {

        var data = google.visualization.arrayToDataTable(%data%);

        var options = {
          title: 'Historical Temp'
        };

        var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="chart_div" style="width: 900px; height: 500px;"></div>
  </body>
</html> """.replace('%data%', displaydata)  



  return data
  ##return '<pre>' + open('temp.data').read()


def get_dbhandle():
    con = None
    con = sqlite3.connect('/var/lib/rpi-datalogger/database.db')
    return con


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0',port=80)
