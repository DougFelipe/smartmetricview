import os
import csv

class ReadCSV:
    def ler_csv_em_metrica(self, caminho_arquivo):
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