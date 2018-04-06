"""
An updated stock ticker dashboard based on Chris Parmer's
2016 PLOTCON talk.
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas_datareader.data as web
import datetime

app = dash.Dash()

app.layout = html.Div([
    html.H3('Enter a stock ticker:'),
    dcc.Input(
        id='my_input',
        value='TSLA'
    ),
    dcc.Graph(
        id='my_graph',
        figure={
            'data': [
                {'x': [1,2], 'y': [3,1]}
            ]
        }
    )
])

@app.callback(
    Output('my_graph', 'figure'),
    [Input('my_input', 'value')])
def update_graph(stock_ticker):
    start = str(datetime.date.today()-datetime.timedelta(days=90))
    end = str(datetime.date.today())
    df = web.DataReader(stock_ticker,'iex',start,end)
    fig = {
        'data': [
            {
                'x': df.index,
                'y': df.open
            }
        ]
    }
    return fig


if __name__ == '__main__':
    app.run_server()
