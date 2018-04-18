#######
# This line chart shows U.S. Census Bureau
# population data from six New England states.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# read a .csv file into a pandas DataFrame:
df = pd.read_csv('../data/population.csv', index_col=0)

# create traces
traces = [go.Scatter(
    x = df.columns,
    y = df.loc[name],
    mode = 'markers+lines',
    name = name
) for name in df.index]

layout = go.Layout(
    title = 'Population Estimates of the Six New England States'
)

fig = go.Figure(data=traces,layout=layout)
pyo.plot(fig, filename='line2.html')
