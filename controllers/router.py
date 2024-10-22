from dash.dependencies import Input, Output
from components.content_view import ContentView
from controllers.content_controller import ContentController

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
        @app.callback(
            Output('page-content', 'children'),
            [Input('url', 'pathname')]
        )
        def display_page(pathname):
            return ContentView().layout()

        # Registra os callbacks do ContentController
        ContentController.register_callbacks(app)
