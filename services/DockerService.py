# services/DockerService.py
import subprocess
import os
from exceptions.CKAnalysisException import CKAnalysisException

class DockerService:
    def run_ck_analysis(self, repo_url):
        """Classe responsável por executar a análise CK"""

        current_directory = os.getcwd()  # Obtém o diretório de trabalho atual
        output_directory = os.path.join(current_directory, "output")  # Define o diretório de saída para os arquivos CSV

        try:
            # Comando para executar o Docker com montagem de volume
            result = subprocess.check_output(
                [
                    'docker', 'run',
                    '-e', f'REPO_URL={repo_url}',
                    '-v', f"{output_directory}:/app/output",  # Monta o diretório de saída do host no container
                    'ck-analyzer'
                ],
                stderr=subprocess.STDOUT
            )
            return result.decode('utf-8')
        except subprocess.CalledProcessError as e:
            raise CKAnalysisException(f"Erro durante a execução do Docker: {e.output.decode('utf-8')}")
