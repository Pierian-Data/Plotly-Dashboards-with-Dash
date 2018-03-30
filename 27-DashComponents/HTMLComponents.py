"""
This provides examples of Dash HTML Components.
Feel free to add things to it that you find useful.
"""
import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    'This is the outermost Div',
    html.Div(
        'This is an inner Div',
        style = {'color':'blue', 'borderWidth':2,
        'borderColor':'blue', 'borderStyle':'solid', 'borderRadius':5,
        'padding':10, 'width':220}
    ),
    html.Div(
        'This is another inner Div',
        style = {'color':'green', 'borderWidth':2,
        'borderColor':'green', 'borderStyle':'solid',
        'margin':10, 'width':220}
    ),

], style={'width':500, 'height':200, 'color':'red', 'borderWidth':2,
'borderColor':'red', 'borderStyle':'dotted'}) # this styles the outermost Div

if __name__ == '__main__':
    app.run_server()
