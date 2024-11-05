# controllers/router.py
from dash import html
from dash.dependencies import Input, Output
from components.content import Content
from components.feedback import FeedbackForm
from components.results_view import ResultsView
from components.loginForm import LoginForm
from components.content_LLM import Content_LLM
from services.auth_services import AuthService

def routes(app):
    content_page = Content(app)
    content_llm_page = Content_LLM(app)
    feedback_page = FeedbackForm(app)
    results_page = ResultsView()
    login_page = LoginForm(app, AuthService())

    @app.callback(
        Output('page-content', 'children'),
        Input('url', 'pathname')
    )
    def display_page(pathname):
        # Verifica se o usuário está autenticado
        if not AuthService.is_authenticated() and pathname != '/login':
            return login_page()  # Redireciona para login se não autenticado
        if pathname == '/feedback':
            return feedback_page()
        elif pathname == '/results':
            return results_page.layout()
        elif pathname == '/llm':
            return content_llm_page()
        elif pathname == '/':
            return content_page()
        elif pathname == '/login':
            return login_page()
        else:
            return html.H1("Página não encontrada", className='error')
