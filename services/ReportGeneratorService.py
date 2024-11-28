# services/ReportGeneratorService.py
from exceptions.ReportGenerationException import ReportGenerationException

from services.DockerService import DockerService
from services.MetricsToTextService import MetricsToTextService
from services.ReadCSVService import ReadCSVService
from services.LLMCKService import LLMCKService
from services.ReportStructuringService import ReportStructuringService

class ReportGeneratorService:
    def __init__(self):
        self.docker = DockerService()
        self.llm_ck = LLMCKService()
        self.readCSV = ReadCSVService()
        self.metrics_to_text = MetricsToTextService()
        self.report_struturing = ReportStructuringService()

    def analyze_and_generate_report(self, url, description):
        if not description:
            raise ReportGenerationException("Por favor escreva uma pequena descrição sobre seu projeto.")

        try:
            # Executa a análise CK
            self.docker.run_ck_analysis(url)
        except Exception as e:
            raise ReportGenerationException(f"Erro ao executar a análise CK: {str(e)}")

        try:
            # Lê os arquivos CSV
            outputclass = self.readCSV.ler_csv_em_metrica('outputclass.csv')
            outputfield = self.readCSV.ler_csv_em_metrica('outputfield.csv')
            outputmethod = self.readCSV.ler_csv_em_metrica('outputmethod.csv')
            outputvariable = self.readCSV.ler_csv_em_metrica('outputvariable.csv')
        except Exception as e:
            raise ReportGenerationException(f"Erro ao ler arquivos CSV: {str(e)}")

        try:
            # Converte as métricas CK para texto
            ck_metrics = self.metrics_to_text.metrics_to_text_convert(
                description_project=description,
                outputclass=outputclass,
                outputfield=outputfield,
                outputmethod=outputmethod,
                outputvariable=outputvariable
            )
        except Exception as e:
            raise ReportGenerationException(f"Erro ao converter métricas CK para texto: {str(e)}")

        try:
            # Realiza a análise LLM-CK
            llm_ck_result = self.llm_ck.perform_llm_ck_analysis(ck_metrics)
        except Exception as e:
            raise ReportGenerationException(f"Erro na análise LLM-CK: {str(e)}")

        try:
            # Estrutura o relatório final
            file_name = "relatorio_projeto.pdf"
            self.report_struturing.structuring_report(
                nome_arquivo=file_name,
                repositorio_url=url,
                description=description,
                ck_metrics=ck_metrics,
                analise_llm_ck=llm_ck_result
            )
        except Exception as e:
            raise ReportGenerationException(f"Erro ao gerar o relatório: {str(e)}")

        return file_name
