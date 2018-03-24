"""
This lineplot uses pandas to reduce a U.S. Census Bureau dataset
down to just six New England states.
"""
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('nst-est2017-alldata.csv')
# grab just the six New England states
df2 = df[df['DIVISION']=='1']
# set the index to state name
df2.set_index('NAME', inplace=True)
# grab just the population columns
df2 = df2[[col for col in df2.columns if col.startswith('POP')]]

pyo.plot([{
    'x': df2.columns,
    'y': df2.loc[name],
    'name': name
} for name in df2.index], filename='line2.html')
