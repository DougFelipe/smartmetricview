<<<<<<< Updated upstream
#components/content.py
=======
#components/content_view.py

>>>>>>> Stashed changes
from dash import html, dcc

class ContentView:
    """
    Classe responsável pela interface de entrada para a análise CK.
    """

    def layout(self):
        """
        Retorna o layout da página de análise CK.
        
        :return: html.Div com o conteúdo da página.
        """
        return html.Div([
            html.Div([
                html.P("Insira o URL do repositório GitHub para análise com a ferramenta CK:"),
                dcc.Input(id='github-url', type='text', placeholder='URL do repositório GitHub'),
                html.Button('Executar Análise', id='execute-button', n_clicks=0),
                html.Div(id='output-container')
            ], className='content-card')
        ])
