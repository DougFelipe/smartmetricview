import csv
from services.docker_service import run_ck_analysis
from services.metrics_to_text_service import MetricsToTextConvert
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import html, dcc
from services.repository_service import clone_repository
from services.llm_ck_service import perform_llm_ck_analysis
import os

def ler_csv_em_metrica(caminho_arquivo):
    # Resolve o caminho absoluto para o arquivo CSV
    caminho_absoluto = os.path.join(os.path.dirname(__file__), '..', 'output', caminho_arquivo)

    # Dicionário para armazenar as métricas extraídas
    metricas_por_classe = {}

    # Verifica se o arquivo existe antes de tentar abrir
    if not os.path.exists(caminho_absoluto):
        raise FileNotFoundError(f"O arquivo {caminho_absoluto} não foi encontrado.")

    # Abre o arquivo CSV
    with open(caminho_absoluto, mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)  # Usando DictReader para facilitar o acesso por nome de coluna

        for linha in leitor_csv:
            # O nome da classe é armazenado na chave 'class'
            classe = linha['class']

            # Adiciona as métricas dessa classe ao dicionário
            metricas_por_classe[classe] = linha

    return metricas_por_classe

def register_callbacks(app):
    @app.callback(
        Output('output-container-llm-ck', 'children'),
        [Input('execute-button-llm-ck', 'n_clicks')],
        [State('github-url-llm-ck', 'value'),  # Captura o URL
         State('description-project', 'value')]  # Captura a descrição do projeto
    )
    def execute_analysis(n_clicks, url, description):
        if n_clicks > 0 and url:
            run_ck_analysis(url)

            # Obtém as métricas dos arquivos CSV
            outputclass = ler_csv_em_metrica('outputclass.csv')
            outputfield = ler_csv_em_metrica('outputfield.csv')
            outputmethod = ler_csv_em_metrica('outputmethod.csv')
            outputvariable = ler_csv_em_metrica('outputvariable.csv')

            metrics_to_text = MetricsToTextConvert()
            text_context = metrics_to_text.metrics_to_text_convert(
                description_project=description,
                outputclass=outputclass,
                outputfield=outputfield,
                outputmethod=outputmethod,
                outputvariable=outputvariable
            )

            print(text_context)
            # Chama a função de análise LLM com o texto concatenado
            llm_result = perform_llm_ck_analysis(text_context)

            # Exibe o resultado em formato Markdown
            llm_analysis = html.Div([
                html.H4("Resultado da Análise com LLM:"),
                dcc.Markdown(llm_result, style={'whiteSpace': 'pre-wrap', 'textAlign': 'left'})
            ], style={'textAlign': 'left'})

            return llm_analysis

        raise PreventUpdate  # services/llm_service.py
