# app.py
from dash import Dash, html, dcc
from components.header import Header
from controllers.router import Router

app = Dash(__name__, suppress_callback_exceptions=True)

# Inicializa o header
header = Header()

# Configura o layout principal
app.layout = html.Div([
    header(),  # Cabeçalho fixo no topo
    dcc.Location(id='url', refresh=False),  # Para controlar as páginas com base no caminho
    html.Div(id='page-content')  # Onde as páginas serão renderizadas
])

# Registro das rotas no aplicativo
Router.register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
