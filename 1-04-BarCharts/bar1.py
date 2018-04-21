#######
# A basic bar chart showing the total number of
# 2018 Winter Olympics Medals won by Country.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/2018WinterOlympics.csv')

data = [go.Bar(
    x=df['NOC'],  # NOC stands for National Olympic Committee
    y=df['Total']
)]
layout = go.Layout(
    title='2018 Winter Olympic Medals by Country'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar1.html')
