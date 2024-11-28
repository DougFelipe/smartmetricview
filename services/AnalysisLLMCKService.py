from dash import html, dcc
from services.DockerService import DockerService
from services.MetricsToTextService import MetricsToTextService
from services.LLMCKService import LLMCKService
from services.ReadCSVService import ReadCSVService
from exceptions.AnalysisLLMCKException import AnalysisLLMCKException

class AnalysisLLMCKService:
    def __init__(self):
        self.readerCSV = ReadCSVService()
        self.docker = DockerService()
        self.metrics_to_text = MetricsToTextService()
        self.llmck = LLMCKService()

    def execute_ck_and_llm_analysis(self, url, description):
        if not url:
            raise AnalysisLLMCKException("URL do repositório GitHub não foi fornecida.")

        if not description:
            raise AnalysisLLMCKException("Por favor escreva uma pequena descrição sobre seu projeto.")

        try:
            self.docker.run_ck_analysis(url)
        except Exception as e:
            raise AnalysisLLMCKException(f"Erro ao executar a análise CK: {str(e)}")

        try:
            outputclass = self.readerCSV.ler_csv_em_metrica('outputclass.csv')
            outputfield = self.readerCSV.ler_csv_em_metrica('outputfield.csv')
            outputmethod = self.readerCSV.ler_csv_em_metrica('outputmethod.csv')
            outputvariable = self.readerCSV.ler_csv_em_metrica('outputvariable.csv')
        except Exception as e:
            raise AnalysisLLMCKException(f"Erro ao processar os arquivos CSV: {str(e)}")

        try:
            text_context = self.metrics_to_text.metrics_to_text_convert(
                description_project=description,
                outputclass=outputclass,
                outputfield=outputfield,
                outputmethod=outputmethod,
                outputvariable=outputvariable
            )
        except Exception as e:
            raise AnalysisLLMCKException(f"Erro ao converter métricas em texto: {str(e)}")

        try:
            llm_result = self.llmck.perform_llm_ck_analysis(text_context)
        except Exception as e:
            raise AnalysisLLMCKException(f"Erro ao executar a análise com LLM: {str(e)}")

        return html.Div([
            html.H4("Resultado da Análise com LLM:"),
            dcc.Markdown(llm_result, style={'whiteSpace': 'pre-wrap', 'textAlign': 'left'})
        ], style={'textAlign': 'left'})
