# app.py
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from components.header import Header  # Importa o Header]
from components.navbar import Navbar
from controllers.router import routes  # Importa a função de registro de rotas

app = Dash(__name__,
           external_stylesheets=[dbc.themes.MINTY],
           suppress_callback_exceptions=True)

# Inicializa o header
header = Header(app)
navbar = Navbar()

app.layout = html.Div([
    header(),
    navbar(),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

routes(app)

if __name__ == '__main__':
    app.run_server(debug=True)
