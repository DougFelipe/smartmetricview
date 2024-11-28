from dash import html


class Header:
    """
    Classe responsável por gerar o cabeçalho do dashboard CK.
    """

    def __init__(self, app):

        self.app = app

    def __call__(self):

        return html.Header(
            html.H1("CK Dashboard Analysis", className="header-title"),
            className="header"
        )
