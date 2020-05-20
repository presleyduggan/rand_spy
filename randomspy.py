import numpy
import pandas as pd
import pandas_datareader as dr
import random as random

spy = []
num = []

num.append(random.randrange(1,506))

data = open("spy.txt")

for position, line in enumerate(data):

    if position in num:
        print(line)

data.close()
