from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from services.docker_service import run_ck_analysis
from services.data_service import create_tables

class ContentController:
    """
    Controlador responsável por gerenciar a lógica de interação na página de análise CK.
    """

    @staticmethod
    def register_callbacks(app):
        """
        Registra os callbacks necessários para a página de análise CK.
        
        :param app: Instância do aplicativo Dash.
        """
        @app.callback(
            Output('output-container', 'children'),
            [Input('execute-button', 'n_clicks')],
            [State('github-url', 'value')]
        )
        def execute_analysis(n_clicks, url):
            if n_clicks > 0 and url:
                # Executa a análise CK
                run_ck_analysis(url)
                # Retorna as tabelas geradas
                return create_tables()  # Cria as tabelas a partir dos dados gerados
            raise PreventUpdate
