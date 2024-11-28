class AnalysisLLMError(Exception):
    """Erro genérico para falhas no processo de análise."""
    def __init__(self, message):
        super().__init__(message)