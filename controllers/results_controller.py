# controllers/results_controller.py

from dash import Input, Output
from services.data_loader import DataLoader
from services.chart_service import ChartService
import plotly.graph_objects as go

data_loader = DataLoader()
chart_service = ChartService()

def register_callbacks(app):
    @app.callback(
        Output('metric-dropdown', 'options'),
        Input('table-dropdown', 'value')
    )
    def update_metrics_options(table_name):
        if table_name:
            metrics = data_loader.get_metrics(table_name)
            return [{'label': metric, 'value': metric} for metric in metrics]
        return []

    @app.callback(
        Output('metric-graph', 'figure'),
        [Input('table-dropdown', 'value'),
         Input('chart-type-dropdown', 'value'),
         Input('metric-dropdown', 'value')]
    )
    def update_graph(table_name, chart_type, metric):
        if table_name and chart_type and metric:
            df = data_loader.load_table(table_name)
            fig = chart_service.generate_chart(df, chart_type, metric)
            return fig
        return go.Figure()  # Retorna um gráfico vazio se as opções estão incompletas
