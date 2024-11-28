from dash import html, dcc
from dash.dependencies import Input, Output, State

from dash.exceptions import PreventUpdate
from services.AnalysisLLMCKService import AnalysisLLMCKService
from exceptions.AnalysisLLMCKException import AnalysisLLMCKException
class AnalysisLLMCKController:

    def register_callbacks(self, app):
        analysis = AnalysisLLMCKService()

        @app.callback(
            Output('output-container-llm-ck', 'children'),
            [Input('execute-button-llm-ck', 'n_clicks')],
            [State('github-url-llm-ck', 'value'),
             State('description-project', 'value')]
        )
        def execute_analysis(n_clicks_analise, url, description):
            if n_clicks_analise > 0:
                try:
                    result = analysis.execute_ck_and_llm_analysis(url, description)
                    return result

                except AnalysisLLMCKException as e:
                    return html.Div(f"Erro: {str(e)}", style={'color': 'red'})

                except Exception as e:
                    return html.Div("Ocorreu um erro inesperado. Tente novamente mais tarde.", style={'color': 'red'})

            raise PreventUpdate
