
class ReportCreationException(Exception):
    """Exceção personalizada para erros no envio de feedback."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
