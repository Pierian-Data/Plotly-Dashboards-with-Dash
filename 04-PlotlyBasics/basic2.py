#######
# This script creates the same type of plot as basic1.py,
# but in Plotly. Note that it creates an .html file!
######
import numpy as np
import pandas as pd
import plotly.offline as pyo

# create fake data:
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
pyo.plot([{
    'x': df.index,
    'y': df[col],
    'name': col
} for col in df.columns])
