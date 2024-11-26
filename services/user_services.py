from services.auth_services import USERS

class UserService:
    def register(self, username, password):
        """
        Registra um novo usuário na memória.
        """
        if username in USERS:
            return False  # Usuário já existe
        USERS[username] = password
        return True
