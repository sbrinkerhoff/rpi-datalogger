#!/usr/bin/python

from flask import *

import os

app = Flask(__name__)

def home():
  return render_template('home.html')

@app.route('/')
@app.route('/temp')
def temp():
  graphdata = []
  filedata = open('/root/temp.data').read()
  for line in filedata.split('\n'):
 
    try: 
      time = line.split(",")[0]
    except:
      continue
    try: 
      inside = line.split(",")[1]
    except:
      continue
    try: 
      outside = line.split(",")[2] 
    except:
      outside = 0 

    graphdata.append("['%s', %s, %s]" % (time,inside,outside))

  
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

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0',port=80)
