# controllers/router.py
from dash.dependencies import Input, Output
from components.content import Content
from components.feedback import FeedbackForm
from components.results_view import ResultsView  # Importa a nova página de resultados
from components.loginForm import LoginForm
from services.auth_services import AuthService
def routes(app):
    content_page = Content(app)
    feedback_page = FeedbackForm(app)
    results_page = ResultsView()  # Cria uma instância da página de resultados
    login_page = LoginForm(app, AuthService())

    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
    )
    def display_page(pathname):
        if pathname == '/feedback':
            return feedback_page()  # Retorna a página de feedback
        elif pathname == '/results':
            return results_page.layout()  # Retorna a página de resultados
        elif pathname == '/':
            return content_page()  # Retorna a página principal (análise CK)
        else:
            return login_page()  # Retorna a página de login
