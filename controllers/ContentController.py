# controllers/ContentController.py
from dash.dependencies import Input, Output, State
from dash import dcc, html
from dash.exceptions import PreventUpdate
from services.DockerService import DockerService
from exceptions.CKAnalysisException import CKAnalysisException

class ContentController:
    def register_callbacks(self, app):
        docker = DockerService()
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
                    try:
                        docker.run_ck_analysis(url)

                        return (
                            html.Div(""),  # Conteúdo do container
                            "Visualizar Resultados",
                            True,
                            {'display': 'inline-block'}
                        )
                    except CKAnalysisException as e:
                        return html.Div(f"Erro: {str(e)}", style={'color': 'red'})
                else:
                    return dcc.Location(pathname='/results', id='redirect'), "Visualizar Resultados", True,  {'display': 'inline-block'}
            raise PreventUpdate
