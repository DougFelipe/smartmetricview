import os
import csv
from exceptions.CSVReadException import CSVReadException


class ReadCSVService:
    def ler_csv_em_metrica(self, caminho_arquivo):
        """Classe responsável por ler as métricas nos arquivos .csv"""

        caminho_absoluto = os.path.join(os.path.dirname(__file__), '..', 'output', caminho_arquivo)

        metricas_por_classe = {}

        try:
            # Verifica se o arquivo existe
            if not os.path.exists(caminho_absoluto):
                raise CSVReadException(f"O arquivo {caminho_absoluto} não foi encontrado.")

            # Abre o arquivo CSV
            with open(caminho_absoluto, mode='r', encoding='utf-8') as arquivo:
                leitor_csv = csv.DictReader(arquivo)

                # Processa as linhas do CSV
                for linha in leitor_csv:
                    classe = linha['class']
                    metricas_por_classe[classe] = linha

        except FileNotFoundError as e:
            raise CSVReadException(f"Erro ao encontrar o arquivo: {str(e)}")
        except csv.Error as e:
            raise CSVReadException(f"Erro ao ler o arquivo CSV: {str(e)}")
        except Exception as e:
            raise CSVReadException(f"Erro inesperado: {str(e)}")

        return metricas_por_classe
