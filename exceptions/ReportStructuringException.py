class ReportStructuringException(Exception):
    """Exceção personalizada para erros na geração do relatório."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)