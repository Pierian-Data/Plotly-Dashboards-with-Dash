import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('data/mpg.csv')

app.layout = html.Div([
    dcc.Graph(
        id='scatter3',
        figure={
            'data': [go.Box(
                y = df[df['model_year']==year]['mpg'],
                name = year+1900,
                boxpoints = 'all'
            ) for year in df['model_year'].unique()],
            'layout': go.Layout(
                title = 'mpg.csv dataset',
                xaxis = {'title': 'Model Year'},
                yaxis = {'title': 'Miles per gallon'},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()
