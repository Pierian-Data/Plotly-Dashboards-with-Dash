import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff
# import plotly.graph_objs as go

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")

table = ff.create_table(df)

pyo.plot(table, filename='table1')
