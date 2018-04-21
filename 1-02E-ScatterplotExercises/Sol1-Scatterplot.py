#######
# Objective: Create a scatterplot of 1000 random data points.
# x-axis values should come from a normal distribution using
# np.random.randn(1000)
# y-axis values should come from a uniform distribution over [0,1) using
# np.random.rand(1000)
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

# obtain x and y values:
random_x = np.random.randn(1000) # normal distribution
random_y = np.random.rand(1000)  # uniform distribution

# define a data variable
data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
)]

# define the layout, and include a title and axis labels
layout = go.Layout(
    title = 'Random Data Scatterplot', # Graph title
    xaxis = dict(title = 'Normal distribution'), # x-axis label
    yaxis = dict(title = 'Uniform distribution'), # y-axis label
    hovermode ='closest' # handles multiple points landing on the same vertical
)

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution1.html')
