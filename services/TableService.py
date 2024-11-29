# services/table_service.py

import os
import pandas as pd
from dash import html
from components.tables import create_table_from_dataframe

class TableService:
    """
    Serviço responsável por carregar arquivos CSV e gerar tabelas.
    """
    def __init__(self, output_dir='output'):
        self.output_dir = output_dir
        self.file_name_map = {
            'outputclass.csv': 'Métricas de Classe',
            'outputfield.csv': 'Métricas de Campo',
            'outputmethod.csv': 'Métricas de Método',
            'outputvariable.csv': 'Métricas de Variável'
        }

    def create_tables(self):
        """
        Carrega os arquivos CSV gerados pela ferramenta CK e cria tabelas AG Grid.

        :return: Lista de tuplas (nome descritivo, tabela).
        """
        try:
            tables = []
            for file_name, friendly_name in self.file_name_map.items():
                file_path = os.path.join(self.output_dir, file_name)
                if os.path.exists(file_path):
                    df = pd.read_csv(file_path)
                    table = create_table_from_dataframe(df, table_id=file_name)
                    tables.append((friendly_name, table))
            return tables
        except Exception as e:
            return [("Erro", html.P(f"Erro ao carregar tabelas: {str(e)}"))]
