# controllers/ExportCSVController.py
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from dash import html
from services.CSVDownloadService import CSVDownloadService
from exceptions.CSVDownloadException import CSVDownloadException

class ExportCSVController:
    def register_callbacks_download_csv(self, app):
        file_service = CSVDownloadService()

        @app.callback(
            Output('output-container-download-csv', 'children'),
            [Input('export-tables-button', 'n_clicks')]  # Botão de download
        )
        def export_CSV(n_clicks):
            if not n_clicks or n_clicks <= 0:
                raise PreventUpdate

            try:
                files = file_service.list_files()

                if files is None:
                    return html.Div("Nenhum arquivo disponível para download.")

                download_links = file_service.generate_download_links(files)

                return html.Div([
                    html.Div(
                        html.A(
                            f"Baixar {file['file']}",
                            href=file['link'],
                            target="_blank",
                            style={'color': 'blue', 'textDecoration': 'underline'}
                        ),
                        style={'margin-bottom': '10px'}
                    )
                    for file in download_links
                ])

            except CSVDownloadException as e:
                return html.Div(f"Erro: {str(e)}", style={'color': 'red'})
            except Exception as e:
                return html.Div(f"Erro desconhecido: {str(e)}", style={'color': 'red'})
