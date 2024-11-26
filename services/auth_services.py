from flask import session

# Lista de usuários armazenada na memória
USERS = {}  # Simula o banco de dados em memória

class AuthService:
    def authenticate(self, username, password):
        """
        Autentica o usuário com base no dicionário USERS.
        """
        if username in USERS and USERS[username] == password:
            session['logged_in'] = True
            session['username'] = username
            return True
        session['logged_in'] = False
        return False

    @staticmethod
    def is_authenticated():
        """
        Verifica se o usuário está autenticado.
        """
        return session.get('logged_in', False)

    @staticmethod
    def logout():
        """
        Realiza o logout do usuário.
        """
        session['logged_in'] = False
        session.pop('username', None)

    @staticmethod
    def register(username, password):
        """
        Registra um novo usuário no dicionário USERS.
        """
        if username in USERS:
            return False  # Nome de usuário já existe
        USERS[username] = password
        return True
