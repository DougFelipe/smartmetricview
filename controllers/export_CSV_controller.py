import os
from dash.dependencies import Input, Output
from dash import html

OUTPUT_FOLDER = "output"

def register_callbacks_download_csv(app):
    @app.callback(
        Output('output-container-download-csv', 'children'),
        [Input('export-tables-button', 'n_clicks')]  # Botão de download
    )
    def export_CSV(n_clicks):
        if n_clicks and n_clicks > 0:
            # Lista todos os arquivos na pasta output
            files = os.listdir(OUTPUT_FOLDER)

            if not files:
                return html.Div("Nenhum arquivo disponível para download.")

            # Gera links de download para cada arquivo
            download_links = [
                html.Div(
                    html.A(
                        f"Baixar {file}",
                        href=f"/downloadCSV/{file}",
                        target="_blank",
                        style={'color': 'blue', 'textDecoration': 'underline'}
                    ),
                    style={'margin-bottom': '10px'}
                )
                for file in files
            ]

            return html.Div(download_links)

        raise PreventUpdate
