from dash import html, dcc

class Content_LLM:
    def __init__(self, app):
        # Registrar callbacks em outro módulo
        from controllers.content_llm_controller import register_callbacks
        register_callbacks(app)

    def __call__(self):
        return html.Div([
            html.Div([
                html.H3("Análise LLM"),
                html.P("Insira o URL do repositório GitHub para análise com a LLM e receber sugestões de melhoras para o código de acordo com o padrão SOLID:"),
                dcc.Input(id='github-url-llm', type='text', placeholder='URL do repositório GitHub'),
                html.Button('Executar Análise', id='execute-button-llm', n_clicks=0),
                html.Div(id='output-container-llm')
            ], className='content-card-llm')
        ])
