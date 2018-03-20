"""
This bar chart resembles a histogram as the data
has already aggregated the frequencies by hour
"""
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../FremontBridgeBicycles.csv')

# Convert the "Date" text column to a Datetime series:
df['Date'] = pd.to_datetime(df['Date'])

# Add a column to hold the hour:
df['Hour']=df['Date'].dt.hour

# Add a column to hold "total traffic"
df['Total']=df['Fremont Bridge West Sidewalk']+df['Fremont Bridge East Sidewalk']

data = [go.Bar(
    x=df['Hour'],
    y=df['Total']
)]

layout = go.Layout(title='Fremont Bridge Bicyle Traffic by Hour')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='basic_histogram.html')
