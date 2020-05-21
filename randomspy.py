import warnings
warnings.filterwarnings('ignore') # ignore pandas depcreciated function warning
import numpy
import pandas as pd
import pandas_datareader as dr
import random as random
import matplotlib.pyplot as plt
import yfinance as yf
import yahoofinancials
from datetime import datetime

def give_change(df):


    length1 = len(df['Close'])

    before = df['Close'][0]
    after = df['Close'][length1-1]
    return ((after-before)/before*100)

spy = []
num = []

num.append(random.randrange(1,506))

data = open("spy.txt")

for position, line in enumerate(data):

    if position in num:
        #print(line)
        name = line.strip()

data.close()

## data reader


""" df = dr.data.get_data_yahoo(name, start='2020-01-01', end ='2020-5-20')
df['Close'].plot()
plt.show()
print(df.info()) """

ticker = yf.Ticker("CBRE")
#print(name)
#print(ticker.info)
#print(ticker.info['shortName'])

now = datetime.date(datetime.now())

#3 month

print(name)

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

