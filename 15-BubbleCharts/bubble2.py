"""
A bubble chart is simply a scatter plot
with the added feature that the size of the
marker can be set by the data
"""
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../mpg.csv')

# Add model year to hover text by creating a DataFrame column:
df['text1']=pd.Series(df['model_year'],dtype=str)
df['text2']="'"+df['text1']+" "+df['name']

data = [go.Scatter(
            x=df['horsepower'],
            y=df['mpg'],
            text=df['text2'],
            mode='markers',
            marker=dict(size=1.5*df['cylinders'])
    )]
layout = go.Layout(
    title='Vehicle mpg vs. horsepower',
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble2.html')
