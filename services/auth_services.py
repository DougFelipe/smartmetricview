# services/auth_service.py

class AuthService:
    def authenticate(self, username, password):
        # Implementar a lógica de autenticação aqui
        # Exemplo: validação fixa (apenas para testes)
        if username == "admin" and password == "1234":
            return True
        return False
