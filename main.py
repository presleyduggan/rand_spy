from flask import Flask
import numpy
import pandas as pd
import pandas_datareader as dr
import random as random
import yfinance as yf
from yahooquery import Ticker

app = Flask(__name__)
@app.route('/')
def printrand():
	num = random.randrange(1,506)
	data = open("spy.txt")
	data = pd.read_csv('spy.txt', header=None)
	name = data.iloc[num][0]

	ticker = yf.Ticker(name)

	blank = '<br/>'

	title = "Your random S&P 500 Stock is"+blank+blank

	newTick = Ticker(name)
	fullname = newTick.price[name]['longName']
	#print(newTick.summary_profile[name])
	about = newTick.summary_profile[name]['longBusinessSummary']

	oneYear = ticker.history(period='1y')
	length = len(oneYear['Close'])
	before = oneYear['Close'][0]
	after = oneYear['Close'][length-1]
	change = round(((after-before)/before*100),2)
	oneY = "1 Year Change = "+str(change)+"%"+blank


	threeMonth = ticker.history(period='3mo')
	length = len(threeMonth['Close'])
	before = threeMonth['Close'][0]
	after = threeMonth['Close'][length-1]
	change = round(((after-before)/before*100),2)
	oneS = "3 Month Change = "+str(change)+"%"+blank

	oneMonth = ticker.history(period='1mo')
	length = len(oneMonth['Close'])
	before = oneMonth['Close'][0]
	after = oneMonth['Close'][length-1]
	change = round(((after-before)/before*100),2)
	twoS = "1 Month Change = "+str(change) +"%"+blank

	oneWeek = ticker.history(period='1wk')
	length = len(oneWeek['Close'])
	before = oneWeek['Close'][0]
	after = oneWeek['Close'][length-1]
	change = round(((after-before)/before*100),2)
	threeS = "1 Week Change = "+str(change) +"%"+blank

	oneDay = ticker.history(period='2d')
	length = len(oneDay['Close'])
	before = oneDay['Close'][0]
	after = oneDay['Close'][length-1]
	change = round(((after-before)/before*100),2)
	fourS = "Today's Change = "+str(change) +"%"+blank
	currentP = "Current Price = $"+str(round(after,2))+blank
	return title+name+blank+fullname+blank+blank+about+blank+blank+currentP+blank+blank+oneY+oneS+twoS+threeS+fourS

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
