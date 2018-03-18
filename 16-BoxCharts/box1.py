import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# set up an array of 20 data points, with 20 for a median
y = [10,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data = [
    go.Box(
        y=y,
        boxpoints='all',
        jitter=0.3,
        pointpos=-1.8
    )
]
pyo.plot(data, filename='box1.html')
