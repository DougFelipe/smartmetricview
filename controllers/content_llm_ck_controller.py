import csv
from services.docker_service import run_ck_analysis
from services.metrics_to_text_service import MetricsToTextConvert
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import html, dcc
from services.repository_service import clone_repository
from services.llm_ck_service import perform_llm_ck_analysis
from services.read_CSV_service import ReadCSV
import os


def register_callbacks(app):
    @app.callback(
        Output('output-container-llm-ck', 'children'),
        [Input('execute-button-llm-ck', 'n_clicks')],
        [State('github-url-llm-ck', 'value'),  # Captura o URL
         State('description-project', 'value')]  # Captura a descrição do projeto
    )
    def execute_analysis(n_clicks_analise, url, description):
        if n_clicks_analise > 0:
            if not url:
                return html.Div("Erro: URL do repositório GitHub não fornecido.", style={'color': 'red'})

            try:
                # Executa a análise CK
                run_ck_analysis(url)

                # Processa os arquivos CSV
                readCSV = ReadCSV()
                outputclass = readCSV.ler_csv_em_metrica('outputclass.csv')
                outputfield = readCSV.ler_csv_em_metrica('outputfield.csv')
                outputmethod = readCSV.ler_csv_em_metrica('outputmethod.csv')
                outputvariable = readCSV.ler_csv_em_metrica('outputvariable.csv')

                # Converte as métricas em texto
                metrics_to_text = MetricsToTextConvert()
                text_context = metrics_to_text.metrics_to_text_convert(
                    description_project=description,
                    outputclass=outputclass,
                    outputfield=outputfield,
                    outputmethod=outputmethod,
                    outputvariable=outputvariable
                )

                # Chama a função de análise LLM com o texto gerado
                llm_result = perform_llm_ck_analysis(text_context)

                # Exibe o resultado da análise LLM
                llm_analysis = html.Div([
                    html.H4("Resultado da Análise com LLM:"),
                    dcc.Markdown(llm_result, style={'whiteSpace': 'pre-wrap', 'textAlign': 'left'})
                ], style={'textAlign': 'left'})

                return llm_analysis

            except FileNotFoundError as e:
                # Erro caso algum arquivo CSV não seja encontrado
                return html.Div(f"Erro: Arquivo CSV não encontrado - {str(e)}", style={'color': 'red'})
            except Exception as e:
                # Captura outros erros
                return html.Div(f"Erro inesperado: {str(e)}", style={'color': 'red'})

        raise PreventUpdate  # Se não for clicado, não atualiza a interface
