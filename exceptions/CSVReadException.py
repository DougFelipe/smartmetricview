
class CSVReadException(Exception):
    """Exceção personalizada para erros no serviço de download de CSV."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
