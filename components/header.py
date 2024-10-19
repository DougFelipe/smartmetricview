# components/header.py

from dash import html

class Header:
    """
    Classe responsável por gerar o cabeçalho do dashboard CK.
    """

    def __init__(self, app):
        """
        Inicializa a classe Header.
        
        :param app: Instância do aplicativo Dash.
        """
        self.app = app

    def __call__(self):
        """
        Retorna o layout do cabeçalho.

        :return: html.Header com o título do dashboard.
        """
        return html.Header(
            html.H1("CK Dashboard Analysis", className="header-title"), 
            className="header"
        )
