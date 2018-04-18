#######
# Objective: Using the file mpg.csv, develop a ScatterPlot
# that compares engine displacement to acceleration.
# Have the vehicle name appear on hover.
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Create a pandas DataFrame from mpg.csv
df = pd.read_csv('../data/mpg.csv')

# Define a data variable
data = [go.Scatter(
            x=df['displacement'],
            y=df['acceleration'],
            text=df['name'],
            mode='markers',
    )]

# Define the layout
layout = go.Layout(
    title='Vehicle acceleration vs. engine displacement',
    hovermode='closest'
)

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution1.html')

#######
# So what happened?? Why is the trend sloping downward?
# Remember that acceleration is the number of seconds to go from 0 to 60mph,
# so fewer seconds means faster acceleration!
######
