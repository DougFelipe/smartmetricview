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
            [
                State('username', 'value'),
                State('user-email', 'value'),
                State('feedback-subject', 'value'),
                State('user-feedback', 'value'),
                State('satisfaction-rating', 'value'),
                State('contact-permission', 'value'),
                State('contact-preference', 'value')
            ]
        )
        def handle_feedback(n_clicks, username, email, subject, feedback, satisfaction, contact_permission, contact_preference):
            if n_clicks > 0:
                if not feedback:
                    return html.P("Por favor, forneça uma descrição do seu feedback.")

                contact_details = ""
                if contact_permission:
                    contact_details = f"Preferência de Contato: {contact_preference}"

                # Processa e salva o feedback usando um serviço
                result = self.feedback_service.submit_feedback({
                    'username': username or "Anônimo",
                    'email': email,
                    'subject': subject,
                    'feedback': feedback,
                    'satisfaction': satisfaction,
                    'contact_permission': bool(contact_permission),
                    'contact_preference': contact_details
                })

                return html.P(result)
            raise PreventUpdate
