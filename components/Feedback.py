from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate  # Corrige o erro de PreventUpdate não definido

class FeedbackForm:
    def __init__(self, app):
        from controllers.FeedbackController import FeedbackController
        feedback_controller = FeedbackController()
        feedback_controller.register_callbacks(app)


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


