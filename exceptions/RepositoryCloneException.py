class RepositoryCloneException(Exception):
    """Exceção personalizada para erros na clonagem de repositórios."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
