#######
# This histogram displays the number of Reddit button presses
# over the two months of their social experiment.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/thebutton_presses.csv')

data = [go.Histogram(
    x=df['press time'],
    nbinsx=60
)]

layout = go.Layout(
    title="Number of presses per timeslot"
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='button_presses2.html')
