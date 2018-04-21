#######
# This histogram has narrower bins than the previous hist1.py
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/mpg.csv')

data = [go.Histogram(
    x=df['mpg'],
    xbins=dict(start=8,end=50,size=1),
)]

layout = go.Layout(
    title="Miles per Gallon Frequencies of<br>\
    1970's Era Vehicles"
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='narrow_histogram.html')
