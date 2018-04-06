import dash
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime

app = dash.Dash()
app.layout = html.Div([
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=datetime(1995, 8, 5),
        max_date_allowed=datetime(2017, 9, 19),
        initial_visible_month=datetime(2017, 8, 5),
        end_date=datetime(2017, 8, 25)
    ),
    html.Div(id='output-container-date-picker-range')
])


@app.callback(
    dash.dependencies.Output('output-container-date-picker-range', 'children'),
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
     dash.dependencies.Input('my-date-picker-range', 'end_date')])
def update_output(start_date, end_date):
    string_prefix = 'You have selected: '
    if start_date is not None:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        start_date_string = start_date.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
    if end_date is not None:
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        end_date_string = end_date.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'End Date: ' + end_date_string
    if len(string_prefix) == len('You have selected: '):
        return 'Select a date to see it displayed here'
    else:
        return string_prefix


if __name__ == '__main__':
    app.run_server()
