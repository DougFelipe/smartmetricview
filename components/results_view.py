# components/results_view.py

from dash import html
import dash_bootstrap_components as dbc
from services.data_service import create_tables

class ResultsView:
    """
    Classe responsável por exibir os resultados da análise CK.
    """

    @staticmethod
    def layout():
        """
        Retorna o layout que exibe as tabelas geradas após a análise,
        com cada tabela dentro de um item de acordeão.
        
        :return: html.Div com o layout das tabelas.
        """
        tables = create_tables()  # Função que cria as tabelas a partir dos arquivos CSV

        # Cria o acordeão para exibir cada tabela em um item
        accordion_items = [
            dbc.AccordionItem(
                table,
                title=file_name,
                className="accordion-item"
            )
            for file_name, table in tables  # Agora deve funcionar corretamente com a lista de tuplas (file_name, table)
        ]

        return html.Div([
            html.H2("Resultados da Análise CK", className="result-header"),
            dbc.Accordion(
                accordion_items, 
                start_collapsed=True,  # Inicia com todos os itens fechados
                flush=True,  # Remove os contornos ao redor do acordeão
                className="table-accordion"
            )
        ], className="results-wrapper")
