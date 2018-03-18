"""
A basic bar chart showing 2018 Winter Olympics Medals
won by Country. Note that the source .csv file is one
directory level higher than this script file.
"""
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Capture the data by reading a table from a webpage:
website = 'https://en.wikipedia.org/wiki/2018_Winter_Olympics#Medal_table'
medals_list = pd.read_html(website,match='Rank',header=0,index_col=1)
df = medals_list[0]

data = [go.Bar(
            x=df['NOC'],
            y=df['Total']
    )]

pyo.plot(data, filename='XXbasic-bar5.html')
