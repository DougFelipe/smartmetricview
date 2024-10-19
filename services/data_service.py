import pandas as pd
import os
from components.tables import create_table_from_dataframe

def create_tables():
    try:
        base_path = os.path.join(os.getcwd(), 'output')
        files = ['outputclass.csv', 'outputfield.csv', 'outputmethod.csv', 'outputvariable.csv']
        tables = []
        for file in files:
            file_path = os.path.join(base_path, file)
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                table = create_table_from_dataframe(df, table_id=file)
                tables.append(table)
        return tables
    except Exception as e:
        return html.P(f"Erro ao carregar tabelas: {str(e)}")
