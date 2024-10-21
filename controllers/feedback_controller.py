#feedback_controller.py

from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from services.feedback_service import FeedbackService
from dash import html

class FeedbackController:
    """
    Controlador responsável por gerenciar a lógica de interação na página de feedback.
    """

    def __init__(self):
        self.feedback_service = FeedbackService()

    def register_callbacks(self, app):
        """
        Registra os callbacks necessários para a página de feedback.
        
        :param app: Instância do aplicativo Dash.
        """
        @app.callback(
            Output('feedback-response', 'children'),
            [Input('send-feedback', 'n_clicks')],
            [State('username', 'value'), State('user-feedback', 'value')]
        )
        def handle_feedback(n_clicks, username, feedback):
            if n_clicks > 0 and feedback:
                result = self.feedback_service.submit_feedback(username, feedback)
                return html.P(result)
            raise PreventUpdate
