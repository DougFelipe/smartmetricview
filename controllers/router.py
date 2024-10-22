from dash.dependencies import Input, Output
from components.content_view import ContentView
from components.feedback_view import FeedbackView
from controllers.content_controller import ContentController
from controllers.feedback_controller import FeedbackController

class Router:
    """
    Controlador responsável pelo roteamento das páginas do dashboard.
    """

    @staticmethod
    def register_callbacks(app):
        """
        Registra os callbacks de navegação entre as páginas e outros necessários.
        
        :param app: Instância do aplicativo Dash.
        """
        # Callback de navegação entre páginas
        @app.callback(
            Output('page-content', 'children'),
            [Input('url', 'pathname')]
        )
        def display_page(pathname):
            if pathname == '/feedback':
                return FeedbackView().layout()  # Retorna o layout da página de feedback
            else:
                return ContentView().layout()  # Retorna o layout da página principal

        # Registra os callbacks dos controladores de conteúdo e feedback
        ContentController.register_callbacks(app)
        FeedbackController().register_callbacks(app)  # Registra os callbacks para feedback
