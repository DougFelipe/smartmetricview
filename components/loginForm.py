# components/login_form.py

from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

class LoginForm:
    def __init__(self, app, auth_service):
        self.auth_service = auth_service
        self.register_callbacks(app)

    def __call__(self):
        return html.Div([
            html.Div([
                html.H3("Login"),
                dcc.Input(
                    id='login-username',
                    type='text',
                    placeholder='Nome de usuário',
                    value='',
                ),
                dcc.Input(
                    id='login-password',
                    type='password',
                    placeholder='Senha',
                    value='',
                ),
                html.Button('Entrar', id='login-button', n_clicks=0),
                html.Div(id='login-response')
            ], className='login-card')  # Aplica a classe CSS "login-card"
        ])

    def register_callbacks(self, app):
        @app.callback(
            Output('login-response', 'children'),
            [Input('login-button', 'n_clicks')],
            [State('login-username', 'value'), State('login-password', 'value')],
           
        )
        def handle_login(n_clicks, username, password):
            if n_clicks > 0:
                if username and password:
                    authenticated = self.auth_service.authenticate(username, password)
                    if authenticated:
                        return dcc.Location(pathname='/content', id='redirect')
                    else:
                        return html.P("Usuário ou senha incorretos.", className='error')
                else:
                    return html.P("Por favor, preencha todos os campos.", className='error')
            raise PreventUpdate
