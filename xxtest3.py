import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
trace1= go.Scatter(x=[0,0.5,1,2,2.2],y=[1.23,2.5,0.42,3,1])
layout= go.Layout(images= [dict(
                  source= "Fremont-Bridge-1.jpg",
                  xref= "x",
                  yref= "y",
                  x= 0,
                  y= 3,
                  sizex= 2,
                  sizey= 2,
                  sizing= "stretch",
                  opacity= 0.5,
                  layer= "below")])
fig=go.Figure(data=[trace1],layout=layout)
pyo.plot(fig)
