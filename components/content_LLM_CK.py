from dash import html, dcc

class Content_LLM_CK:
    def __init__(self, app):
        # Registrar callbacks em outro módulo
        from controllers.content_llm_ck_controller import register_callbacks
        register_callbacks(app)

    def __call__(self):
        return html.Div([
            html.Div([
                html.H3("Análise LLM - Analise CK"),
                html.P("Insira o URL do repositório GitHub para análise com a LLM e receber sugestões de melhoras para o código de acordo com a Analise CK:"),
                dcc.Input(id='github-url-llm-ck', type='text', placeholder='URL do repositório GitHub'),
                dcc.Input(id='description-project', type='text', placeholder='Faça uma breve descrição do projeto'),
                html.Button('Executar Análise', id='execute-button-llm-ck', n_clicks=0),
                html.Div(id='output-container-llm-ck')
            ], className='content-card-llm-ck')
        ])
