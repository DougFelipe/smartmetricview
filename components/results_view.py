from dash import html, dcc
import dash_bootstrap_components as dbc
from services.data_service import create_tables
from services.data_loader import DataLoader


class ResultsView:
    """
    Classe responsável por exibir os resultados da análise CK e a interface para visualização de gráficos.
    """

    @staticmethod
    def layout():
        """
        Retorna o layout contendo as tabelas no acordeão e os controles de visualização de gráficos.

        :return: html.Div com o layout completo.
        """
        tables = create_tables()  # Função que cria as tabelas a partir dos arquivos CSV
        data_loader = DataLoader()  # Instância para carregar tabelas e métricas

        # Cria o acordeão para exibir cada tabela em um item
        accordion_items = [
            dbc.AccordionItem(
                table,
                title=file_name,  # Nome descritivo da tabela
                className="accordion-item"
            )
            for file_name, table in tables
        ]

        # Dropdowns para seleção de tabela, tipo de gráfico e métrica
        table_dropdown = dcc.Dropdown(
            id='table-dropdown',
            options=[{'label': name, 'value': name} for name in data_loader.get_table_names()],
            placeholder="Selecione uma tabela"
        )

        chart_type_dropdown = dcc.Dropdown(
            id='chart-type-dropdown',
            options=[
                {'label': 'Linha', 'value': 'line'},
                {'label': 'Barras', 'value': 'bar'},
                {'label': 'Box', 'value': 'box'},
                {'label': 'Histograma', 'value': 'histogram'}
            ],
            placeholder="Selecione um tipo de gráfico"
        )

        metric_dropdown = dcc.Dropdown(
            id='metric-dropdown',
            placeholder="Selecione uma métrica"
        )

        return html.Div([
            html.H2("Resultados da Análise CK", className="result-header"),

            # Acordeão com as tabelas
            dbc.Accordion(
                accordion_items,
                start_collapsed=True,
                always_open=True,
                flush=False,
                className="table-accordion"
            ),

            # Seção de visualização de gráficos
            html.H3("Visualização de Gráficos", className="chart-header"),
            html.Div([
                html.Label("Tabela"),
                table_dropdown,
                html.Label("Tipo de Gráfico"),
                chart_type_dropdown,
                html.Label("Métrica"),
                metric_dropdown,
                html.Div(id="graph-container")  # Onde o gráfico será exibido
            ], className="chart-controls"),
        ], className="results-wrapper")
