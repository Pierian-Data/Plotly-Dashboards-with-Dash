"""
Scatterplot of Old Faithful Geyser Eruption data
obtained from Duke University Statistics Lab
at http://www2.stat.duke.edu/courses/Fall03/sta290/datasets.html
"""
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/OldFaithful.csv')

data = [go.Scatter(
    x = df['X'],
    y = df['Y'],
    mode = 'markers'
)]
layout = go.Layout(
    title = 'Old Faithful Eruption Intervals v Durations', # Graph title
    xaxis = dict(title = 'Duration of eruption (minutes)'), # x-axis label
    yaxis = dict(title = 'Interval to next eruption (minutes)'), # y-axis label
    hovermode ='closest' # handles multiple points landing on the same vertical
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='OldFaithfulPlot.html')
