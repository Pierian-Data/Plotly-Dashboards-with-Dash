#######
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd 
# Create a DataFrame from  "flights" data
df = pd.read_csv('../data/flights.csv')

# Define a data variable
data = [go.Heatmap(
    x=df['year'],
    y=df['month'],
    z=df['passengers']
)]

# Define the layout
layout = go.Layout(
    title='Flights'
)
# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution8.html')

#######
# Excellent! This shows two distinct trends - an increase in
# passengers flying over the years, and a greater number of
# passengers flying in the summer months.
######
