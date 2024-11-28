import os
from select import select
from dash import html, dcc

from exceptions.AnalysisLLMException import AnalysisLLMError
from services.CloneRepositoryService import CloneRepositoryService
from services.LLMSolidService import LLMSolidService
from services.RepositoryReaderService import RepositoryReaderService

class AnalysisLLMService:
    def __init__(self):
        self.clone_repo = CloneRepositoryService()
        self.repo_reader = RepositoryReaderService()
        self.llm_solid = LLMSolidService()

    def clone_and_analyze_repository(self, url):
        """Excuta a Analise LLM com o projeto fornecido"""

        if not url:
            raise AnalysisLLMError("URL do repositório GitHub não foi fornecida.")

        try:
            repo_path = self.clone_repo.clone_repository(url)
            if isinstance(repo_path, str) and "Erro" in repo_path:
                raise AnalysisLLMError(repo_path)
        except Exception as e:
            raise AnalysisLLMError(f"Erro ao clonar repositório: {str(e)}")

        try:
            code = self.repo_reader.read_code(repo_path)
        except Exception as e:
            raise AnalysisLLMError(f"Erro ao ler código do repositório: {str(e)}")

        try:
            result = self.llm_solid.perform_llm_analysis(code)
        except Exception as e:
            raise AnalysisLLMError(f"Erro ao executar análise LLM: {str(e)}")

        llm_analysis = html.Div([
            html.H4("Resultado da Análise com LLM:"),
            dcc.Markdown(result, style={'whiteSpace': 'pre-wrap', 'textAlign': 'left'})
        ], style={'textAlign': 'left'})

        return llm_analysis

