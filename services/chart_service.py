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
