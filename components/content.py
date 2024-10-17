# components/content.py

from dash import html,dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import os
from components.tables import create_table_from_dataframe

class Content:
    def __init__(self, app):
        self.app = app
        self.register_callbacks(app)

    def __call__(self):
        return html.Div([
            html.Div([
                html.P("Insira o URL do repositório GitHub para análise com a ferramenta CK:"),
                dcc.Input(id='github-url', type='text', placeholder='URL do repositório GitHub'),
                html.Button('Executar Análise', id='execute-button', n_clicks=0),
                html.Div(id='output-container')
            ], className='content-card')
        ])

    def register_callbacks(self, app):
        @app.callback(
            Output('output-container', 'children'),
            [Input('execute-button', 'n_clicks')],
            [State('github-url', 'value')]
        )
        def execute_analysis(n_clicks, url):
            if n_clicks > 0 and url:
                result = run_ck_analysis(url)
                return self.create_tables()
            raise PreventUpdate

    def create_tables(self):
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
            return html.Div(tables)
        except Exception as e:
            return html.P(f"Erro ao carregar tabelas: {str(e)}")

# Lembre-se de importar a função run_ck_analysis se ela estiver definida em outro módulo.
from services.docker_service import run_ck_analysis