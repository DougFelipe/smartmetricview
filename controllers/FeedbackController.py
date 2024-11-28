# controllers/FeedbackController.py
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import html
from services.FeedbackService import FeedbackService
from exceptions.FeedbackSubmissionException import FeedbackSubmissionException

class FeedbackController:
    def register_callbacks(self, app):
        self.feedback_service = FeedbackService()

        @app.callback( 
            Output('feedback-response', 'children'),
            [Input('send-feedback', 'n_clicks')],
            [State('username', 'value'), State('user-feedback', 'value')]
        )
        def handle_feedback(n_clicks, username, feedback):
            if n_clicks > 0:
                if feedback:
                    try:
                        result = self.feedback_service.submit_feedback(username, feedback)
                        return html.P(result, className='success')
                    except FeedbackSubmissionException as e:
                        return html.P(f"Erro: {str(e)}", className='error')
                else:
                    return html.P("Por favor, escreva um feedback.", className='error')
            raise PreventUpdate
