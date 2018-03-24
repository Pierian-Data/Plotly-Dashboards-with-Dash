"""
A basic bar chart showing 2018 Winter Olympic Medals
won by Country.
"""
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Capture the data by reading a table from a webpage:
website = 'https://en.wikipedia.org/wiki/2018_Winter_Olympics#Medal_table'
medals_list = pd.read_html(website,match='Rank',header=0,index_col=1)
df = medals_list[0]

data = [go.Bar(
            x=df['NOC'],
            y=df['Total']
    )]

pyo.plot(data, filename='bar4.html')
