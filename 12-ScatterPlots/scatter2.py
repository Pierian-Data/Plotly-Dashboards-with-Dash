import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd

N = 100
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

# Create traces
trace0 = go.Scatter(
    x = random_x,
    y = random_y+5,
    mode = 'markers',
    name = 'markers'
)
trace1 = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'lines+markers',
    name = 'lines+markers'
)
trace2 = go.Scatter(
    x = random_x,
    y = random_y-5,
    mode = 'lines',
    name = 'lines'
)

data = [trace0, trace1, trace2]
pyo.plot(data, filename='scatter-mode.html')
