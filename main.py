from flask import Flask
import numpy
import pandas as pd
import pandas_datareader as dr
import random as random

app = Flask(__name__)
@app.route('/')

def printrand():
spy = []
num = []
num.append(random.randrange(1,506))
data = open("spy.txt")
for position, line in enumerate(data):
    if position in num:
        print(line)
data.close()

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)
