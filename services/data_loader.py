import pandas as pd
import os

class DataLoader:
    def __init__(self, output_dir='output'):
        self.output_dir = output_dir
        
        # Dicionário de mapeamento para nomes descritivos
        self.tables = {
            'Classes': 'outputclass.csv',
            'Fields': 'outputfield.csv',
            'Methods': 'outputmethod.csv',
            'Variables': 'outputvariable.csv'
        }

    def get_table_names(self):
        # Retorna uma lista dos nomes amigáveis das tabelas
        return list(self.tables.keys())

    def load_table(self, table_name):
        file_path = os.path.join(self.output_dir, self.tables[table_name])
        if os.path.exists(file_path):
            return pd.read_csv(file_path)
        return pd.DataFrame()  # Retorna um DataFrame vazio se o arquivo não for encontrado

    def get_metrics(self, table_name):
        # Retorna as colunas (métricas) disponíveis em uma tabela específica
        df = self.load_table(table_name)
        return df.columns.tolist()
