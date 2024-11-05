from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import html, dcc  # Importa dcc para usar o Markdown
from services.repository_service import clone_repository
from services.llm_service import perform_llm_analysis
import os

def read_code_from_repository(repo_path):
    code = ""
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.java'):  # Adapte a extensão conforme necessário
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    code += f.read() + "\n\n"  # Adiciona o código e uma nova linha para separação
    return code

def register_callbacks(app):
    @app.callback(
        Output('output-container-llm', 'children'),
        [Input('execute-button-llm', 'n_clicks')],
        [State('github-url-llm', 'value')]
    )
    def execute_analysis(n_clicks, url):
        if n_clicks > 0 and url:
            repo_path = clone_repository(url)
            if isinstance(repo_path, str) and "Erro" in repo_path:
                return html.P(repo_path)  # Retorna o erro caso o clone falhe

            code = read_code_from_repository(repo_path)

            llm_result = perform_llm_analysis(code)

            # Exibe o resultado em formato Markdown
            llm_analysis = html.Div([
                html.H4("Resultado da Análise com LLM:"),
                dcc.Markdown(llm_result, style={'whiteSpace': 'pre-wrap', 'textAlign': 'left'})
            ], style={'textAlign': 'left'})

            return llm_analysis

        raise PreventUpdate
