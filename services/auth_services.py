# services/auth_services.py
from flask import session

class AuthService:
    def authenticate(self, username, password):
        # Lógica de autenticação básica para testes
        if username == "admin" and password == "1234":
            session['logged_in'] = True
            session['username'] = username
            return True
        session['logged_in'] = False
        return False

    @staticmethod
    def is_authenticated():
        return session.get('logged_in', False)

    @staticmethod
    def logout():
        session['logged_in'] = False
        session.pop('username', None)
