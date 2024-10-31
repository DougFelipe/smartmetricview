# controllers/content_controller.py

from dash.dependencies import Input, Output, State
from dash import dcc
from dash.exceptions import PreventUpdate
from services.docker_service import run_ck_analysis

def register_callbacks(app):
    @app.callback(
        [Output('output-container', 'children'),
         Output('execute-button', 'children'),
         Output('analysis-complete', 'data')],
        [Input('execute-button', 'n_clicks')],
        [State('github-url', 'value'),
         State('analysis-complete', 'data')]
    )
    def execute_analysis(n_clicks, url, analysis_complete):
        if n_clicks > 0:
            if not analysis_complete:
                # Executa a análise CK
                run_ck_analysis(url)  # Executa a análise e salva os dados nos arquivos CSV
                
                # Altera o botão para "Visualizar Resultados" e atualiza o estado de análise
                return "", "Visualizar Resultados", True
            else:
                # Redireciona para a página de resultados
                return dcc.Location(pathname='/results', id='redirect'), "Visualizar Resultados", True
        raise PreventUpdate
