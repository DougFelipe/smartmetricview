#components/feedback.py

from dash import html, dcc

class FeedbackView:
    """
    Classe responsável pela interface de feedback do usuário.
    """

    def layout(self):
        """
        Retorna o layout da página de feedback.
        
        :return: html.Div com o formulário de feedback.
        """
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
