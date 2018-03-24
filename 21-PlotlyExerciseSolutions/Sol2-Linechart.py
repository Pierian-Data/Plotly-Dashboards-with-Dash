"""
Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
that plots seven days worth of temperature data on one graph.
You can use a for loop to assign each day to its own trace.
"""
# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Create a pandas DataFrame from mpg.csv
df = pd.read_csv('../2010YumaAZ.csv')

# Define a data variable
data = [pyo.plot([{
    'x': df['LST_TIME'],
    'y': df['T_HR_AVG'],
    'name': day
} for day in df['DAY']])]

# Define the layout
layout = go.Layout(
    title='Daily temperatures from June 1 - June 7, 2010 in Yuma, Arizona',
    hovermode='closest'
)

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution2.html')
