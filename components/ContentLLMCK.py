from dash import html, dcc

class ContentLLMCK:
    def __init__(self, app):
        # Registrar callbacks em outro módulo
        from controllers.AnalysisLLMCKController import AnalysisLLMCKController
        from controllers.ReportController import ReportController
        controller_analysis = AnalysisLLMCKController()
        controller_analysis.register_callbacks(app)

        controller_report = ReportController()
        controller_report.register_callbacks_download(app)  # Registrar os callbacks do download, caso haja um módulo separado para isso

    def __call__(self):
        return html.Div([
            html.Div([
                html.H3("Análise LLM - Analise CK"),
                html.P("Insira o URL do repositório GitHub para análise com a LLM e receber sugestões de melhoras para o código de acordo com a Analise CK:"),
                dcc.Input(id='github-url-llm-ck', type='text', placeholder='URL do repositório GitHub'),
                dcc.Input(id='description-project', type='text', placeholder='Faça uma breve descrição do projeto'),
                html.Button('Executar Análise', id='execute-button-llm-ck', n_clicks=0),
                html.Button("Gerar Relatório", id='download-button', n_clicks=0),
                html.Div(id='output-container-llm-ck'),
                html.Div(id='output-container-download')
            ], className='content-card-llm-ck')
        ])
