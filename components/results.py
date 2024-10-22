from dash import html
from services.data_service import create_tables

class ResultsView:
    """
    Classe responsável por exibir os resultados da análise CK,
    que são as tabelas geradas após a execução.
    """

    @staticmethod
    def layout():
        """
        Retorna o layout que exibe as tabelas geradas após a análise.
        
        :return: html.Div com o layout das tabelas.
        """
        tables = create_tables()  # Função que cria as tabelas a partir dos arquivos CSV
        return html.Div([
            html.H2("Resultados da Análise CK", className="result-header"),
            html.Div(tables, className="table-container")  # Envolvemos as tabelas em um contêiner
        ], className="results-wrapper")  # Classe geral para o layout
