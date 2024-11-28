# controllers/router.py
from dash import html
from dash.dependencies import Input, Output
from components.Content import Content
from components.Feedback import FeedbackForm
from components.results_view import ResultsView
from components.loginForm import LoginForm
from components.ContentLLM import ContentLLM
from components.ContentLLMCK import ContentLLMCK
from components.registerForm import RegisterForm
from services.auth_services import AuthService
from services.user_services import UserService
from controllers.results_controller import register_callbacks  # Importa a função de registro de callbacks
import os
from flask import Flask, send_from_directory


def routes(app):
    content_page = Content(app)
    content_llm_page = ContentLLM(app)
    content_llm_ck_page = ContentLLMCK(app)
    feedback_page = FeedbackForm(app)
    results_page = ResultsView()
    login_page = LoginForm(app, AuthService())
    register_form = RegisterForm(app, UserService())
    

    # Registra os callbacks específicos de results_controller
    register_callbacks(app)  # Registra os callbacks de gráfico

    # Define o caminho para o diretório de downloads
    DOWNLOAD_DIRECTORY = os.getenv("DOWNLOAD_DIRECTORY")
    if not os.path.exists(DOWNLOAD_DIRECTORY):
        os.makedirs(DOWNLOAD_DIRECTORY)

    @app.server.route('/download/<filename>')
    def download_file(filename):
        try:
            # Verifica se o arquivo existe no diretório
            file_path = os.path.join(DOWNLOAD_DIRECTORY, filename)
            if not os.path.exists(file_path):
                return f"Arquivo {filename} não encontrado.", 404

            # Usa send_from_directory para enviar o arquivo
            return send_from_directory(directory=DOWNLOAD_DIRECTORY, path=filename, as_attachment=True)

        except Exception as e:
            return f"Erro ao enviar o arquivo: {str(e)}", 500



    # Caminho absoluto da pasta onde os arquivos estão armazenados
    OUTPUT_FOLDER = os.path.join(os.getcwd(), "output")

    @app.server.route('/downloadCSV/<filename>')
    def export_csv(filename):
        try:
            # Verifica se o arquivo existe no diretório
            file_path = os.path.join(OUTPUT_FOLDER, filename)
            if not os.path.exists(file_path):
                return abort(404, description=f"Arquivo {filename} não encontrado.")

            # Usa send_from_directory para enviar o arquivo
            return send_from_directory(directory=OUTPUT_FOLDER, path=filename, as_attachment=True)

        except Exception as e:
            # Loga o erro no console (para depuração) e retorna uma mensagem genérica ao usuário
            print(f"Erro ao enviar o arquivo: {str(e)}")
            return abort(500, description="Erro interno ao processar o arquivo.")


    @app.callback(
        Output('page-content', 'children'),
        Input('url', 'pathname')
    )
    def display_page(pathname):
        # Verifica se o usuário está autenticado
        if not AuthService.is_authenticated() and pathname not in ['/login', '/register']:
            return login_page()
        if pathname == '/feedback':
            return feedback_page()
        elif pathname == '/results':
            return results_page.layout()
        elif pathname == '/llm':
            return content_llm_page()
        elif pathname == '/llm_ck':
            return content_llm_ck_page()
        elif pathname == '/':
            return content_page()
        elif pathname == '/login':
            return login_page()
        elif pathname == '/register':
            return register_form.layout()
        else:
            return html.H1("Página não encontrada", className='error')
