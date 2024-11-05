# components/loginForm.py
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from flask import session
import dash

class LoginForm:
    def __init__(self, app, auth_service):
        self.auth_service = auth_service
        self.register_callbacks(app)

    def __call__(self):
        return html.Div([
            html.H3("Login"),
            dcc.Input(id='login-username', type='text', placeholder='Nome de usuário'),
            dcc.Input(id='login-password', type='password', placeholder='Senha'),
            html.Button('Entrar', id='login-button', n_clicks=0),
            html.Div(id='login-response')
        ], className='login-card')

    def register_callbacks(self, app):
        @app.callback(
            [Output('login-response', 'children'), Output('url', 'pathname')],
            Input('login-button', 'n_clicks'),
            State('login-username', 'value'),
            State('login-password', 'value')
        )
        def handle_login(n_clicks, username, password):
            if n_clicks > 0:
                if username and password:
                    authenticated = self.auth_service.authenticate(username, password)
                    if authenticated:
                        # Redireciona para a página principal após o login bem-sucedido
                        return "", "/"
                    else:
                        return html.P("Usuário ou senha incorretos.", className='error'), dash.no_update
                else:
                    return html.P("Por favor, preencha todos os campos.", className='error'), dash.no_update
            raise PreventUpdate
