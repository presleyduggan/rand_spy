from flask import Flask
import numpy
import pandas as pd
import pandas_datareader as dr
import random as random
import yfinance as yf

app = Flask(__name__)
@app.route('/')
def printrand():
  num = []
  num.append(random.randrange(1,506))
  data = open("spy.txt")
  for position, line in enumerate(data):
      if position in num:
          name = (line.strip())
  data.close()

  print(name)
  ticker = yf.Ticker(name)

  blank = '<br/>'

  threeMonth = ticker.history(period='3mo')
  length = len(threeMonth['Close'])
  before = threeMonth['Close'][0]
  after = threeMonth['Close'][length-1]
  change = ((after-before)/before*100)
  oneS = "3 Month Change = "+str(change)+blank


  oneMonth = ticker.history(period='1mo')
  length = len(oneMonth['Close'])
  before = oneMonth['Close'][0]
  after = oneMonth['Close'][length-1]
  change = ((after-before)/before*100)
  twoS = "1 Month Change = "+str(change) +blank



  oneWeek = ticker.history(period='1wk')
  length = len(oneWeek['Close'])
  before = oneWeek['Close'][0]
  after = oneWeek['Close'][length-1]
  change = ((after-before)/before*100)
  threeS = "1 Week Change = "+str(change) +blank



  oneDay = ticker.history(period='2d')
  length = len(oneDay['Close'])
  before = oneDay['Close'][0]
  after = oneDay['Close'][length-1]
  change = ((after-before)/before*100)
  fourS = "Today's Change = "+str(change) +blank
  return name+blank+blank+oneS+twoS+threeS+fourS

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)
