df = dr.data.get_data_yahoo(name, start='2020-01-01', end ='2020-5-20')
df['Close'].plot()
plt.show()
print(df.info())