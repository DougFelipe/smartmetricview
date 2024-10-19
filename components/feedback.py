from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate  # Corrige o erro de PreventUpdate não definido
from services.feedback_service import FeedbackService

class FeedbackForm:
    def __init__(self, app):
        self.app = app
        self.feedback_service = FeedbackService()
        self.register_callbacks(app)

    def __call__(self):
        return html.Div([
            html.Div([
                html.H3("Deixe seu Feedback"),
                dcc.Input(
                    id='username',
                    type='text',
                    placeholder='Seu Nome',
                    value=''
                ),
                dcc.Textarea(
                    id='user-feedback',
                    placeholder='Escreva seu feedback aqui...',
                    style={'width': '100%', 'height': 200},
                    value=''
                ),
                html.Button('Enviar Feedback', id='send-feedback', n_clicks=0),
                html.Div(id='feedback-response')
            ], className='feedback-card')
        ])

    def register_callbacks(self, app):
        @app.callback(
            Output('feedback-response', 'children'),
            [Input('send-feedback', 'n_clicks')],
            [State('username', 'value'), State('user-feedback', 'value')]
        )
        def handle_feedback(n_clicks, username, feedback):
            if n_clicks > 0 and feedback:
                # Usa o serviço de feedback para processar e salvar o feedback
                result = self.feedback_service.submit_feedback(username, feedback)
                return html.P(result)
            # Evita que a callback seja disparada caso não haja cliques
            raise PreventUpdate
