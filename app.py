# app.py
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate  # Importar PreventUpdate
from components.content import Content
from components.feedback import FeedbackForm
from components.header import Header  # Importa o Header

app = Dash(__name__, suppress_callback_exceptions=True)

# Inicializa as páginas e o header
content_page = Content(app)
feedback_page = FeedbackForm(app)
header = Header(app)

app.layout = html.Div([
    header(),  # Adiciona o header no layout acima das páginas
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/feedback':
        return feedback_page()  # Retorna a página de feedback
    else:
        return content_page()  # Retorna a página principal (análise CK)

if __name__ == '__main__':
    app.run_server(debug=True)
