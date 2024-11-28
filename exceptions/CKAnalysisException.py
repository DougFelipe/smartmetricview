class CKAnalysisException(Exception):
    """Exceção personalizada para erros no serviço Docker."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
