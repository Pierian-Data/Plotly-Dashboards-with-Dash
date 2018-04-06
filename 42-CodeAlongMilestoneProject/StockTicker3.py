"""
First Milestone Project: Develop a Stock Ticker
dashboard that either allows the user to enter
a ticker symbol into an input box, or to select
item(s) from a dropdown list, and uses pandas_datareader
to look up and display stock data on a graph.
"""
# DEVELOP THE GRAPH LAYOUT FIRST, AND LEAVE THE CALLBACK FOR THE NEXT PHASE
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader.data as web
import datetime

app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H3('Enter a stock ticker:'),
    dcc.Input(
        id='my_input',
        value='TSLA' # sets a default value
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
    start = datetime.datetime(2017, 1, 1)
    end = datetime.datetime(2017, 12, 31)
    df = web.DataReader(stock_ticker,'iex',start,end)
    fig = {
        'data': [
            {'x': df.index, 'y': df.close}
        ],
        'layout': {'title':stock_ticker}
    }
    return fig

if __name__ == '__main__':
    app.run_server()
