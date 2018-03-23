"""
This distplot uses plotly's Figure Factory
module in place of Graph Objects
"""
import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

x = np.random.randn(1000)
data = [x]
group_labels = ['distplot']

fig = ff.create_distplot(data, group_labels)
pyo.plot(fig, filename='basic_distplot.html')
