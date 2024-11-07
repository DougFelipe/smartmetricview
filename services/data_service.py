# services/data_service.py

from dash import html
import pandas as pd
import os
from components.tables import create_table_from_dataframe

def create_tables():
    """
    Carrega os arquivos CSV gerados pela ferramenta CK e cria tabelas AG Grid,
    retornando uma lista de tuplas com o nome descritivo e a tabela gerada.

    :return: Lista de tuplas (nome descritivo, tabela).
    """
    try:
        base_path = os.path.join(os.getcwd(), 'output')
        
        # Dicionário de mapeamento para nomes descritivos
        file_name_map = {
            'outputclass.csv': 'Métricas de Classe',
            'outputfield.csv': 'Métricas de Campo',
            'outputmethod.csv': 'Métricas de Método',
            'outputvariable.csv': 'Métricas de Variável'
        }
        
        files = file_name_map.keys()  # Os arquivos a serem carregados com base nas chaves do dicionário
        tables = []
        
        for file in files:
            file_path = os.path.join(base_path, file)
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                table = create_table_from_dataframe(df, table_id=file)
                
                # Use o nome amigável do dicionário ao invés do nome do arquivo
                friendly_name = file_name_map[file]
                tables.append((friendly_name, table))
        
        return tables
    
    except Exception as e:
        return [("Erro", html.P(f"Erro ao carregar tabelas: {str(e)}"))]


import plotly.graph_objects as go

class ChartService:
    def generate_chart(self, df, chart_type, metric):
        if df.empty or metric not in df.columns:
            return go.Figure()  # Retorna um gráfico vazio se os dados estão ausentes

        if chart_type == 'line':
            fig = go.Figure(go.Scatter(x=df.index, y=df[metric], mode='lines', name=metric))
        elif chart_type == 'bar':
            fig = go.Figure(go.Bar(x=df.index, y=df[metric], name=metric))
        elif chart_type == 'box':
            fig = go.Figure(go.Box(y=df[metric], name=metric))
        elif chart_type == 'histogram':
            fig = go.Figure(go.Histogram(x=df[metric], name=metric))
        else:
            fig = go.Figure()  # Caso padrão para evitar erro em caso de tipo inválido

        fig.update_layout(title=f'{metric} - {chart_type.capitalize()}')
        return fig
