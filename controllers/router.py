# controllers/router.py
from dash.dependencies import Input, Output
from components.content import Content
from components.feedback import FeedbackForm
from components.results_view import ResultsView  # Importa a nova página de resultados

def routes(app):
    content_page = Content(app)
    feedback_page = FeedbackForm(app)
    results_page = ResultsView()  # Cria uma instância da página de resultados

    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
    )
    def display_page(pathname):
        if pathname == '/feedback':
            return feedback_page()  # Retorna a página de feedback
        elif pathname == '/results':
            return results_page.layout()  # Retorna a página de resultados
        else:
            return content_page()  # Retorna a página principal (análise CK)
