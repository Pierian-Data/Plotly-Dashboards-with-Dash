import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash('')

app.layout = html.Div([
    dcc.RadioItems(
        id='dropdown-a',
        options=[{'label': i, 'value': i} for i in ['Canada', 'USA', 'Mexico']],
        value='Canada'
    ),
    html.Div(id='output-a'),

    dcc.RadioItems(
        id='dropdown-b',
        options=[{'label': i, 'value': i} for i in ['MTL', 'NYC', 'SF']],
        value='MTL'
    ),
    html.Div(id='output-b')

])


@app.callback(
    dash.dependencies.Output('output-a', 'children'),
    [dash.dependencies.Input('dropdown-a', 'value')])
def callback_a(dropdown_value):
    return 'You\'ve selected "{}"'.format(dropdown_value)


@app.callback(
    dash.dependencies.Output('output-b', 'children'),
    [dash.dependencies.Input('dropdown-b', 'value')])
def callback_b(dropdown_value):
    return 'You\'ve selected "{}"'.format(dropdown_value)


if __name__ == '__main__':
    app.run_server()
