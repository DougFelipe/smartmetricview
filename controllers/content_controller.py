# controllers/content_controller.py
from dash.dependencies import Input, Output, State
from dash import dcc, html
from dash.exceptions import PreventUpdate
from services.docker_service import run_ck_analysis


def register_callbacks(app):
    @app.callback(
        [
            Output('output-container', 'children'),
            Output('execute-button', 'children'),
            Output('analysis-complete', 'data'),
            Output('export-tables-button', 'style')  # Adicionando novo Output
        ],
        [Input('execute-button', 'n_clicks')],
        [State('github-url', 'value'),
         State('analysis-complete', 'data')]
    )
    def execute_analysis(n_clicks, url, analysis_complete):
        if n_clicks > 0:
            if not analysis_complete:
                run_ck_analysis(url)

                # Retorna os valores necessários
                return (
                    html.Div(""),  # Conteúdo do container
                    "Visualizar Resultados",
                    True,
                    {'display': 'inline-block'}
                )
            else:
                # Redireciona para a página de resultados
                return dcc.Location(pathname='/results', id='redirect'), "Visualizar Resultados", True,  {'display': 'inline-block'}
        raise PreventUpdate
