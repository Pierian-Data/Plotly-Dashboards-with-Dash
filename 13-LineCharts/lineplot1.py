import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('https://www2.census.gov/programs-surveys/popest/datasets/2010-2017/national/totals/nst-est2017-alldata.csv')
df2 = df[df['DIVISION']=='1']  # grab just the six New England states
df2.set_index('NAME', inplace=True) # set the index to state name
df2 = df2[[col for col in df2.columns if col.startswith('POP')]] # grab just the population columns

pyo.plot([{
    'x': df2.columns,
    'y': df2.loc[name],
    'name': name
} for name in df2.index])
