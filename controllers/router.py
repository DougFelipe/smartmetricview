# controllers/router.py
from dash.dependencies import Input, Output
from components.content import Content
from components.feedback import FeedbackForm

def routes(app):
    content_page = Content(app)
    feedback_page = FeedbackForm(app)

    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
    )
    def display_page(pathname):
        if pathname == '/feedback':
            return feedback_page()  # Retorna a página de feedback
        else:
            return content_page()  # Retorna a página principal (análise CK)
