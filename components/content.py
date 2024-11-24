# components/content.py

from dash import html, dcc

class Content:
    def __init__(self, app):
        from controllers.content_controller import register_callbacks
        from controllers.export_CSV_controller import register_callbacks_download_csv
        register_callbacks(app)
        register_callbacks_download_csv(app)


    def __call__(self):
        return html.Div([
            dcc.Store(id='analysis-complete', data=False),  # Armazena o estado da análise
            html.Div([
                html.H3("Análise CK"),
                html.P("Insira o URL do repositório GitHub para análise com a ferramenta CK:"),
                dcc.Input(id='github-url', type='text', placeholder='URL do repositório GitHub'),
                html.Button('Executar Análise', id='execute-button', n_clicks=0),
                html.Div(id='output-container'),

                # Botão "Exportar Tabelas" inicialmente oculto
                html.Button("Exportar Tabelas", id="export-tables-button", style={'display': 'none'}),
                html.Div(id='output-container-download-csv')

            ], className='content-card')
        ])
