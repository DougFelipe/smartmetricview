from dash.dependencies import Input, Output
from components.content_view import ContentView
from components.feedback_view import FeedbackView
from controllers.content_controller import ContentController

class Router:
    """
    Controlador responsável pelo roteamento das páginas do dashboard.
    """

    @staticmethod
    def register_callbacks(app):
        """
        Registra os callbacks de navegação entre as páginas.
        
        :param app: Instância do aplicativo Dash.
        """
        # Callback para a navegação entre as páginas
        @app.callback(
            Output('page-content', 'children'),
            [Input('url', 'pathname')]
        )
        def display_page(pathname):
            if pathname == '/feedback':
                return FeedbackView().layout()  # Retorna a página de feedback
            else:
                return ContentView().layout()  # Retorna a página principal (análise CK)
        
        # Registra os callbacks do ContentController
        ContentController.register_callbacks(app)  # Certifique-se de que esse método foi chamado
