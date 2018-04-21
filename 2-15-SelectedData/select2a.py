#######
# Here we'll make a scatter plot with fake data that is
# intentionally denser on the left, with overlapping data points.
# We'll use Selection Data to uncover the difference.
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import json

app = dash.Dash()

# create x and y arrays
np.random.seed(10)
x1 = np.linspace(0.1,5,50)
x2 = np.linspace(5.1,10,50)
y = np.random.randint(0,50,50)

# create three "half DataFrames"
df1 = pd.DataFrame({'x': x1, 'y': y})
df2 = pd.DataFrame({'x': x1, 'y': y})
df3 = pd.DataFrame({'x': x2, 'y': y})

# combine them into one DataFrame
df = pd.concat([df1,df2,df3])

app.layout = html.Div([
    html.Div([
    dcc.Graph(
        id='plot',
        figure={
            'data': [
                go.Scatter(
                    x = df['x'],
                    y = df['y'],
                    mode = 'markers'
                )
            ],
            'layout': go.Layout(
                title = 'Random Scatterplot',
                hovermode='closest'
            )
        }
    )], style={'width':'30%', 'display':'inline-block'}),

    html.Div([
    html.Pre(id='density', style={'paddingTop':25})
    ], style={'width':'30%', 'display':'inline-block', 'verticalAlign':'top'})
])

@app.callback(
    Output('density', 'children'),
    [Input('plot', 'selectedData')])
def return_json(selectedData):
    return json.dumps(selectedData, indent=2)

if __name__ == '__main__':
    app.run_server()
