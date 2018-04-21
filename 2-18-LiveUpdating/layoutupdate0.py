#######
# This page doesn't update.
######
import dash
import dash_html_components as html

app = dash.Dash()

crash_free = 0
crash_free += 1

app.layout = html.H1('Crash free for {} refreshes'.format(crash_free))

if __name__ == '__main__':
    app.run_server()
