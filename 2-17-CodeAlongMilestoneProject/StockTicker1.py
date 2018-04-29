#######
# First Milestone Project: Develop a Stock Ticker
# dashboard that either allows the user to enter
# a ticker symbol into an input box, or to select
# item(s) from a dropdown list, and uses pandas_datareader
# to look up and display stock data on a graph.
######

# DEVELOP THE GRAPH LAYOUT FIRST, AND LEAVE THE CALLBACK FOR THE NEXT PHASE
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H3('Enter a stock symbol:'),
    dcc.Input(
        id='my_stock_ticker'
        value='TSLA' # sets a default value
    ),
    dcc.Graph(
        id='my_graph'
        figure={
            'data': [
                {'x': [1,2], 'y': [3,1]}
            ]
        }
    )
])

if __name__ == '__main__':
    app.run_server()
