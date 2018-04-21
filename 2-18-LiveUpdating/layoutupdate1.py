#######
# This page updates when refreshed.
######
import dash
import dash_html_components as html
from datetime import datetime

app = dash.Dash()

def update_layout():
    return html.H1('The time is: ' + str(datetime.now()))

app.layout = update_layout

if __name__ == '__main__':
    app.run_server()
