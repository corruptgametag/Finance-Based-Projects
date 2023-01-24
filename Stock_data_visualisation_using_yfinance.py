import numpy as np
import pandas as pd
import matplotlib as plt
import yfinance as yf
import plotly.express as px


#Getting stock information

tesla = yf.Ticker('TSLA')
print(tesla.history(period='max'))

#Visualising stock data
tesla = yf.download('TSLA', period='max', interval='1d')
tesla_price_chart = px.line(tesla['Close'], title='Tesla Daily Close Price',
                            color_discrete_map={'Close':'green'}, width=800, height=800)
tesla_price_chart.show()

#Plotting the volume graph for Tesla stock as well
tesla_volume_chart = px.area(tesla['Volume'],
                            title='Tesla Daily Volume',
                            color_discrete_map={'Volume':'red'},
                            width=800, height=400)
tesla_volume_chart.show()

#Taking Tesla's closing price data and divide it by the very first closing price (can be found with iloc function)
tesla_pctchange_inception = tesla['Close']/tesla['Close'].iloc[0]
print(tesla_pctchange_inception.head())

#Plotting the Tesla stock price percentage change based on the data again.
tesla_pctchange_chart = px.area(tesla_pctchange_inception,
                           title='Tesla Daily Close Price',
                           width=800, height=800)
tesla_pctchange_chart.show()


