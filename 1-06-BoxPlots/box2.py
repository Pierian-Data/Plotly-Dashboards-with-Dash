#######
# This simple box plot displays outliers
# above and below the box.
######
import plotly.offline as pyo
import plotly.graph_objs as go

# set up an array of 20 data points, with 20 as the median value
y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data = [
    go.Box(
        y=y,
        boxpoints='outliers' # display only outlying data points
    )
]
pyo.plot(data, filename='box2.html')
