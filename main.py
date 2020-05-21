from flask import Flask
import numpy
import pandas as pd
import pandas_datareader as dr
import random as random
import yfinance as yf

def give_change(df):
    length = len(df['Close'])
    before = df['Close'][0]
    after = df['Close'][length-1]
    return ((after-before)/before*100)


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

  threeMonth = ticker.history(period='3mo')
  threeChange = give_change(threeMonth)
  print("3 Month Change = "+str(threeChange))
  oneMonth = ticker.history(period='1mo')
  oneChange = give_change(oneMonth)
  print("1 Month Change = "+str(oneChange))
  oneWeek = ticker.history(period='1wk')
  weekChange = give_change(oneWeek)
  print("1 Month Change = "+str(weekChange))
  oneDay = ticker.history(period='2d')
  dayChange = give_change(oneDay)
  print("Today's Change = "+str(dayChange))

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)
