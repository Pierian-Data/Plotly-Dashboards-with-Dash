#######
# This script will make regular API calls to http://data-live.flightradar24.com
# to obtain updated total worldwide flights data.
# **This version only loads the site. No callbacks.**
######
import dash
import dash_html_components as html
import requests

url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})  # A fake header is necessary to access the site
data = res.json()
counter = 0
for element in data["stats"]["total"]:
    counter += data["stats"]["total"][element]

app = dash.Dash()

app.layout = html.Div([
    html.Div([
        html.Iframe(src = 'https://www.flightradar24.com', height = 500, width = 1200)
    ]),

    html.Div([
    html.Pre('Active flights worldwide: {}'.format(counter))
    ])
])

if __name__ == '__main__':
    app.run_server()
