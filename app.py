# app.py

import dash
from dash import html
from components.header import Header
from components.content import Content

app = dash.Dash(__name__)
app.layout = html.Div([
    Header(app)(),
    Content(app)()
])

if __name__ == '__main__':
    app.run_server(debug=True)
