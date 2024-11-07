from dash import Input, Output
from dash import dcc, html
import plotly.express as px
from services.data_loader import DataLoader

data_loader = DataLoader()

def register_callbacks(app):
    # Callback para atualizar o dropdown de métricas com base na tabela selecionada
    @app.callback(
        Output('metric-dropdown', 'options'),
        Input('table-dropdown', 'value')
    )
    def update_metric_dropdown(selected_table):
        if selected_table:
            metrics = data_loader.get_metrics(selected_table)
            return [{'label': metric, 'value': metric} for metric in metrics]
        return []

    # Callback para atualizar o gráfico com base nos valores selecionados
    @app.callback(
        Output('graph-container', 'children'),
        [Input('table-dropdown', 'value'),
         Input('chart-type-dropdown', 'value'),
         Input('metric-dropdown', 'value')]
    )
    def update_graph(selected_table, chart_type, selected_metric):
        if selected_table and chart_type and selected_metric:
            df = data_loader.load_table(selected_table)
            if chart_type == 'line':
                fig = px.line(df, x=selected_metric, y=df.index)
            elif chart_type == 'bar':
                fig = px.bar(df, x=selected_metric, y=df.index)
            elif chart_type == 'box':
                fig = px.box(df, y=selected_metric)
            elif chart_type == 'histogram':
                fig = px.histogram(df, x=selected_metric)
            return dcc.Graph(figure=fig)
        return html.Div("Selecione uma tabela, um tipo de gráfico e uma métrica para visualizar.")
