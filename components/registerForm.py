from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

class RegisterForm:
    def __init__(self, app, user_service):
        self.user_service = user_service
        self.register_callbacks(app)

    def layout(self):
        return html.Div([
            html.Div([
                html.H3("Cadastro de Usuário"),
                dcc.Input(
                    id='register-username',
                    type='text',
                    placeholder='Nome de usuário',
                    value='',
                ),
                dcc.Input(
                    id='register-password',
                    type='password',
                    placeholder='Senha',
                    value='',
                ),
                html.Button('Cadastrar', id='register-button', n_clicks=0),
                html.Div(id='register-response')
            ], className='register-card')  # Aplica a classe CSS "register-card"
        ])

    def register_callbacks(self, app):
        @app.callback(
            Output('register-response', 'children'),
            [Input('register-button', 'n_clicks')],
            [State('register-username', 'value'), State('register-password', 'value')],
            
        )
        def handle_register(n_clicks, username, password):
            if n_clicks > 0:
                if username and password:
                    success = self.user_service.register(username, password)
                    if success:
                        return html.P("Cadastro realizado com sucesso!", className='success')
                    else:
                        return html.P("Erro ao realizar cadastro. Tente novamente.", className='error')
                else:
                    return html.P("Por favor, preencha todos os campos.", className='error')
            raise PreventUpdate