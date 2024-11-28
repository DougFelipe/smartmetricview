from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from exceptions.AnalysisLLMException import AnalysisLLMError
from services.AnalysisLLMService import AnalysisLLMService


class AnalysisLLMController:
    def register_callbacks(self, app):
        self.analysis_service = AnalysisLLMService()
        @app.callback(
            Output('output-container-llm', 'children'),
            [Input('execute-button-llm', 'n_clicks')],
            [State('github-url-llm', 'value')]
        )

        def process_analysis(n_clicks, url):
            if n_clicks > 0 and url:
                try:
                    result = self.analysis_service.clone_and_analyze_repository(url)
                    return result

                except AnalysisLLMError as e:
                    return f"Erro durante a análise: {e}"

                except Exception as e:
                    return f"Erro inesperado: {str(e)}"



