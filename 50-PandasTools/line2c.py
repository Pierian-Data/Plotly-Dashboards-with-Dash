#######
# This line chart shows U.S. Census Bureau
# population data from six New England states.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# read a .csv file into a pandas DataFrame:
df = pd.read_csv('../data/population.csv')

# Create traces
trace0 = go.Scatter(
    x = df.columns[1:],
    y = df.iloc[0][1:],
    mode = 'markers+lines',
    name = df.iloc[0]['Name']
)
trace1 = go.Scatter(
    x = df.columns[1:],
    y = df.iloc[1][1:],
    mode = 'markers+lines',
    name = df.iloc[1]['Name']
)
trace2 = go.Scatter(
    x = df.columns[1:],
    y = df.iloc[2][1:],
    mode = 'markers+lines',
    name = df.iloc[2]['Name']
)
trace3 = go.Scatter(
    x = df.columns[1:],
    y = df.iloc[3][1:],
    mode = 'markers+lines',
    name = df.iloc[3]['Name']
)
trace4 = go.Scatter(
    x = df.columns[1:],
    y = df.iloc[4][1:],
    mode = 'markers+lines',
    name = df.iloc[4]['Name']
)
trace5 = go.Scatter(
    x = df.columns[1:],
    y = df.iloc[5][1:],
    mode = 'markers+lines',
    name = df.iloc[5]['Name']
)
data = [trace0, trace1, trace2, trace3, trace4, trace5]
layout = go.Layout(
    title = 'Population Estimates of the Six New England States'
)
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='line2.html')
