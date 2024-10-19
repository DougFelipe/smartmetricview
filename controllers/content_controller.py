from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from services.docker_service import run_ck_analysis
from services.data_service import create_tables

def register_callbacks(app):
    @app.callback(
        Output('output-container', 'children'),
        [Input('execute-button', 'n_clicks')],
        [State('github-url', 'value')]
    )
    def execute_analysis(n_clicks, url):
        if n_clicks > 0 and url:
            result = run_ck_analysis(url)
            return create_tables()  # Agora a lógica de criar tabelas está em outro módulo
        raise PreventUpdate
