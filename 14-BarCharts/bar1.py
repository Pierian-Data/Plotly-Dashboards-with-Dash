"""
A basic bar chart showing 2018 Winter Olympics Medals
won by Country. Note that the source .csv file is one
directory level higher than this script file.
"""
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../2018WinterOlympics.csv')

data = [go.Bar(
            x=df['Country'],
            y=df['Total']
    )]

pyo.plot(data, filename='basic-bar1.html')
