import os
from services.docker_service import run_ck_analysis
from services.metrics_to_text_service import MetricsToTextConvert
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import html, dcc
from services.repository_service import clone_repository
from services.llm_ck_service import perform_llm_ck_analysis
from services.llm_service import perform_llm_analysis
from services.read_CSV_service import ReadCSV
from services.report_generator_service import ReportGenerator


def register_callbacks_download(app):
    @app.callback(
        Output('output-container-download', 'children', allow_duplicate=True),
        [Input('download-button', 'n_clicks')],  # Botão de download
        [State('github-url-llm-ck', 'value'),  # Captura o URL
         State('description-project', 'value')], # Captura a descrição do projeto
        prevent_initial_call = 'initial_duplicate'  # Permite duplicação com inicialização duplicada
    )
    def generate_report(n_clicks, url, description):
        if n_clicks <= 0 or not url:
            return html.P("Por favor, forneça a URL do repositório GitHub e clique em 'Gerar Relatório' para gerar o relatório.")

        # Inicia a análise CK
        try:
            run_ck_analysis(url)
        except Exception as e:
            return html.P(f"Erro ao executar a análise CK: {str(e)}", style={'color': 'red'})


        # Obtém as métricas dos arquivos CSV
        try:
            readCSV = ReadCSV()
            outputclass = readCSV.ler_csv_em_metrica('outputclass.csv')
            outputfield = readCSV.ler_csv_em_metrica('outputfield.csv')
            outputmethod = readCSV.ler_csv_em_metrica('outputmethod.csv')
            outputvariable = readCSV.ler_csv_em_metrica('outputvariable.csv')
        except Exception as e:
            return html.P(f"Erro ao ler arquivos CSV: {str(e)}", style={'color': 'red'})


        # Estruturação de métricas
        metrics_to_text = MetricsToTextConvert()
        ck_metrics = metrics_to_text.metrics_to_text_convert(
            description_project=description,
            outputclass=outputclass,
            outputfield=outputfield,
            outputmethod=outputmethod,
            outputvariable=outputvariable
        )


        # Realiza a análise LLM com CK
        try:
            llm_ck_result = perform_llm_ck_analysis(ck_metrics)
        except Exception as e:
            return html.P(f"Erro na análise LLM CK: {str(e)}", style={'color': 'red'})


        # Gera o relatório
        try:
            report_generator = ReportGenerator()
            file_name = "relatorio_projeto.pdf"
            report_generator.generate_report(
                nome_arquivo=file_name,
                repositorio_url=url,
                description=description,
                ck_metrics=ck_metrics,
                analise_llm_ck=llm_ck_result
            )
        except Exception as e:
            return html.P(f"Erro ao gerar o relatório: {str(e)}", style={'color': 'red'})


        # Retorna um link para download do relatório
        return html.Div([
            html.A("Clique aqui para baixar o relatório",
                   href=f"/download/{file_name}",
                   target="_blank",
                   style={'color': 'blue', 'textDecoration': 'underline'})
        ])
