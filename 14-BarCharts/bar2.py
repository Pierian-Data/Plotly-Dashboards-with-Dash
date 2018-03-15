import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../2018WinterOlympics.csv')

data = [go.Bar(
            x=df['Country'],
            y=df['Total']
    )]
layout = go.Layout(
    title='2018 Winter Olympics - Medals by Country'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='basic-bar2.html')
