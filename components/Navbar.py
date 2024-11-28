from dash import html, dcc

class Navbar:
    """
    Classe responsável por gerar a barra de navegação do dashboard CK.
    """

    def __init__(self):
      
        self.links = [
            {'name': 'Análise CK', 'path': '/'},
            {'name': 'Analise LLM + SOLID', 'path': '/llm'},
            {'name': 'Analise LLM + CK', 'path': '/llm_ck'},
            {'name': 'Feedback', 'path': '/feedback'},
            {'name': 'Cadastrar Usuário', 'path': '/register'}
        ]

    def __call__(self):

        return html.Nav(
            className="navbar",
            children=[
                dcc.Link(
                    link['name'],
                    href=link['path'],
                    className="nav-link"
                ) for link in self.links
            ]
        )
