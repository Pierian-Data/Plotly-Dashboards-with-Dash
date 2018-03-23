"""
A bubble chart is simply a scatter plot
with the added feature that the size of the
marker can be set by the data
"""
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../mpg.csv')

data = [go.Scatter(
            x=df['horsepower'],
            y=df['mpg'],
            text=df['name'],
            mode='markers',
            marker=dict(size=1.5*df['cylinders'])
    )]

layout = go.Layout(
    title='Vehicle mpg vs. horsepower',
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble1.html')
