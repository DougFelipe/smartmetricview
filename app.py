# app.py
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from components.header import Header
from components.navbar import Navbar
from components.loginForm import LoginForm
from controllers.router import routes
from services.auth_services import AuthService

app = Dash(__name__,
           external_stylesheets=[dbc.themes.MINTY],
           suppress_callback_exceptions=True)

# Inicializa o header, navbar e auth_service
header = Header(app)
navbar = Navbar()
auth_service = AuthService()
login_form = LoginForm(app, auth_service)


app.layout = html.Div([
    header(),
    navbar(),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=login_form())  # Exibe o formulário de login
])

routes(app)

if __name__ == '__main__':
    app.run_server(debug=True)
