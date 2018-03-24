"""
This plots 500 points from 0 to 1 against random
y-axis values that are normal about zero.
"""
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd

N = 500
x = np.linspace(0, 1, N)
y = np.random.randn(N)
df = pd.DataFrame({'x': x, 'y': y})

pyo.plot({
    "data": [go.Scatter(x=df['x'], y=df['y'],mode='markers')],
    "layout": go.Layout(title="simple scatter")
})
