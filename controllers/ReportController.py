# controllers/ReportController.py
from dash.dependencies import Input, Output, State
from dash import html
from dash.exceptions import PreventUpdate
from services.ReportGeneratorService import ReportGeneratorService

from exceptions.ReportGenerationException import ReportGenerationException



class ReportController:
    def register_callbacks_download(self, app):
        @app.callback(
            Output('output-container-download', 'children', allow_duplicate=True),
            [Input('download-button', 'n_clicks')],  # Botão de download
            [State('github-url-llm-ck', 'value'),  # Captura o URL
             State('description-project', 'value')],  # Captura a descrição do projeto
            prevent_initial_call='initial_duplicate'  # Permite duplicação com inicialização duplicada
        )
        def generate_report(n_clicks, url, description):
            if n_clicks > 0:
                if not url:
                    return html.P(
                        "Por favor, forneça a URL do repositório GitHub e clique em 'Gerar Relatório' para gerar o relatório.")

                try:
                    report_generator = ReportGeneratorService()
                    file_name = report_generator.analyze_and_generate_report(url, description)
                except ReportGenerationException as e:
                    return html.P(f"Erro: {str(e)}", style={'color': 'red'})
                except Exception as e:
                    return html.P(f"Erro inesperado: {str(e)}", style={'color': 'red'})

                return html.Div([
                    html.A("Clique aqui para baixar o relatório",
                           href=f"/download/{file_name}",
                           target="_blank",
                           style={'color': 'blue', 'textDecoration': 'underline'})
                ])
