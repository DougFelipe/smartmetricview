from dash import html, dcc

class Navbar:
    """
    Classe responsável por gerar a barra de navegação do dashboard CK.
    """

    def __init__(self):
        """
        Inicializa a classe Navbar.
        """
        self.links = [
            {'name': 'Análise CK', 'path': '/'},
            {'name': 'Analise LLM', 'path': '/llm'},
            {'name': 'Feedback', 'path': '/feedback'},
        ]

    def __call__(self):
        """
        Retorna o layout da barra de navegação.

        :return: html.Nav com links de navegação.
        """
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
