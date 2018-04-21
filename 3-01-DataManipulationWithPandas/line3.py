#######
# This line chart uses pandas to reduce a U.S. Census Bureau
# dataset down to just six New England states.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# read a .csv file into a pandas DataFrame:
df = pd.read_csv('../sourcedata/nst-est2017-alldata.csv')
# grab just the six New England states:
df2 = df[df['DIVISION']=='1']
# set the index to state name:
df2.set_index('NAME', inplace=True)
# grab just the population columns:
df2 = df2[[col for col in df2.columns if col.startswith('POP')]]

# pass data (use a list comprehension to build traces) into pyo.plot directly
pyo.plot([go.Scatter(
    x = df2.columns,
    y = df2.loc[name],
    mode = 'markers+lines',
    name = name
) for name in df2.index], filename='line3.html')
