# services/data_service.py

from dash import html
import pandas as pd
import os
from components.tables import create_table_from_dataframe

def create_tables():
    """
    Carrega os arquivos CSV gerados pela ferramenta CK e cria tabelas AG Grid,
    retornando uma lista de tuplas com o nome do arquivo e a tabela gerada.

    :return: Lista de tuplas (nome do arquivo, tabela).
    """
    try:
        base_path = os.path.join(os.getcwd(), 'output')
        files = ['outputclass.csv', 'outputfield.csv', 'outputmethod.csv', 'outputvariable.csv']
        tables = []
        
        for file in files:
            file_path = os.path.join(base_path, file)
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                table = create_table_from_dataframe(df, table_id=file)
                tables.append((file, table))  # Adiciona o nome do arquivo junto com a tabela gerada
        
        return tables
    
    except Exception as e:
        return [("Erro", html.P(f"Erro ao carregar tabelas: {str(e)}"))]
