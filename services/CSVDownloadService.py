# services/CSVDownloadService.py
import os
from exceptions.CSVDownloadException import CSVDownloadException  # Importa a exceção personalizada

OUTPUT_FOLDER = "output"

class CSVDownloadService:
    def __init__(self, output_folder=OUTPUT_FOLDER):
        self.output_folder = output_folder

    def list_files(self):
        """Lista os arquivos na pasta de saída."""
        try:
            files = os.listdir(self.output_folder)
            if not files:
                return None
            return files
        except FileNotFoundError as e:
            raise CSVDownloadException(f"Erro ao acessar a pasta de saída: {str(e)}")
        except Exception as e:
            raise CSVDownloadException(f"Erro desconhecido ao listar arquivos: {str(e)}")

    def generate_download_links(self, files):
        """Gera os links de download para os arquivos."""
        try:
            download_links = [
                {
                    'file': file,
                    'link': f"/downloadCSV/{file}"
                }
                for file in files
            ]
            return download_links
        except Exception as e:
            raise CSVDownloadException(f"Erro ao gerar links de download: {str(e)}")
