
class ReportGenerationException(Exception):
    """Exceção personalizada para erros de análise LLM e CK."""
    def __init__(self, message, *args):
        super().__init__(message, *args)
        self.message = message
