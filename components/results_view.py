from dash import html, dcc
import dash_bootstrap_components as dbc
from services.data_loader import DataLoader

class ResultsView:
    @staticmethod
    def layout():
        # Inicializa as tabelas para gerar o conteúdo dinâmico dos dropdowns
        data_loader = DataLoader()
        table_names = data_loader.get_table_names()

        return html.Div([
            html.H2("Resultados da Análise CK", className="result-header"),
            dbc.Accordion(
                [dbc.AccordionItem(html.Div(f"Tabela: {name}"), title=name) for name in table_names],
                start_collapsed=True,
                always_open=True,
                flush=False,
                className="table-accordion"
            ),
            html.Div(id='graph-controls', children=[
                html.H4("Visualização de Gráficos"),
                dcc.Dropdown(
                    id='table-dropdown',
                    options=[{'label': name, 'value': name} for name in table_names],
                    placeholder="Selecione uma tabela"
                ),
                dcc.Dropdown(
                    id='chart-type-dropdown',
                    options=[
                        {'label': 'Linha', 'value': 'line'},
                        {'label': 'Barras', 'value': 'bar'},
                        {'label': 'Box Plot', 'value': 'box'},
                        {'label': 'Histograma', 'value': 'histogram'}
                    ],
                    placeholder="Selecione o tipo de gráfico"
                ),
                dcc.Dropdown(
                    id='metric-dropdown',
                    placeholder="Selecione uma métrica"
                ),
                dcc.Graph(id='metric-graph')
            ], className="graph-controls")
        ])
