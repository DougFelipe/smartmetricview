# components/header.py

from dash import html, dcc

class Header:
    """
    Classe responsável por gerar o cabeçalho do dashboard CK.
    Inclui o nome da ferramenta à esquerda e os botões 'Início' e 'Feedback' à direita.
    """

    def __call__(self):
        """
        Retorna o layout do cabeçalho com o nome da ferramenta à esquerda
        e os botões de navegação no canto direito.

        :return: html.Header contendo o título do dashboard, botão 'Início' e 'Feedback'.
        """
        return html.Header([
            # Div para o nome da ferramenta à esquerda
            html.Div(
                html.H1("CK Dashboard Analysis", className="header-title"),
                className="header-left"
            ),
            # Div para os botões 'Início' e 'Feedback' à direita
            html.Div([
                dcc.Link(
                    html.Button("Início", className="home-button"),
                    href='/',
                    className="nav-link"
                ),
                dcc.Link(
                    html.Button("Feedback", className="feedback-button"),
                    href='/feedback',
                    className="nav-link"
                )
            ], className="header-right")
        ], className="header")
