"""
A basic bar chart showing 2018 Winter Olympics Medals
won by Country. Note that the source .csv file is one
directory level higher than this script file.
"""
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Capture the data by reading a table from a webpage:
website = 'http://www.pyeongchang2018.com/en/game-time/results/OWG2018/en/general/medal-standings.htm'
medals_list = pd.read_html(website,match='Rank',header=0)
df = medals_list[0]

data = [go.Bar(
            x=df['NOC'],
            y=df['Total']
    )]

pyo.plot(data, filename='XXbasic-bar6.html')
