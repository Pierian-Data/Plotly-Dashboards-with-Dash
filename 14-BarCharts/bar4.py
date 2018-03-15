"""
This is a stacked bar chart showing three traces
(gold, silver and bronze medals) for each country
"""
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../2018WinterOlympics.csv')

trace1 = go.Bar(
            x=df['Country'],
            y=df['Gold'],
            name = 'Gold',
            marker=dict(color='#FFD700')
)
trace2 = go.Bar(
            x=df['Country'],
            y=df['Silver'],
            name='Silver',
            marker=dict(color='#9EA0A1')
)
trace3 = go.Bar(
            x=df['Country'],
            y=df['Bronze'],
            name='Bronze',
            marker=dict(color='#CD7F32')
)
data = [trace1, trace2, trace3]
layout = go.Layout(
    title='2018 Winter Olympics - Medals by Country',
    barmode='stack'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='basic-bar4.html')
