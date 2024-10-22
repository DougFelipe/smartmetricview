from dash.dependencies import Input, Output, State
from services.docker_service import run_ck_analysis
from components.results import ResultsView

class ContentController:
    @staticmethod
    def register_callbacks(app):
        @app.callback(
            Output('output-container', 'children'),
            [Input('execute-button', 'n_clicks')],
            [State('github-url', 'value')]
        )
        def execute_analysis(n_clicks, url):
            if n_clicks > 0 and url:
                # Executa a análise CK
                run_ck_analysis(url)
                
                # Carrega o layout dos resultados
                return ResultsView.layout()
            raise PreventUpdate
