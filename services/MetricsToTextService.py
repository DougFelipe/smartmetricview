from exceptions.MetricsStructuringException import MetricsStructuringException

class MetricsToTextService:
    def metrics_to_text_convert(self, description_project, outputclass, outputfield, outputmethod, outputvariable):
        """Classe responsável por estruturar as métricas lidas no .csv em uma string"""
        try:
            text_context = f"Descrição do Projeto: {description_project}\n\n\n"

            text_context += "Métricas das Classes:\n"
            for classe, metrics in outputclass.items():
                text_context += f"\nClasse: {classe}\n"
                for metrica, valor in metrics.items():
                    if metrica != 'class':  # Exclui a coluna 'class'
                        text_context += f"  {metrica}: {valor}\n"

            text_context += "\nMétricas dos Campos (Fields):\n"
            for classe, metrics in outputfield.items():
                text_context += f"\nClasse: {classe}\n"
                for metrica, valor in metrics.items():
                    if metrica != 'class':
                        text_context += f"  {metrica}: {valor}\n"

            text_context += "\nMétricas dos Métodos (Methods):\n"
            for classe, metrics in outputmethod.items():
                text_context += f"\nClasse: {classe}\n"
                for metrica, valor in metrics.items():
                    if metrica != 'class':
                        text_context += f"  {metrica}: {valor}\n"

            text_context += "\nMétricas das Variáveis (Variables):\n"
            for classe, metrics in outputvariable.items():
                text_context += f"\nClasse: {classe}\n"
                for metrica, valor in metrics.items():
                    if metrica != 'class':
                        text_context += f"  {metrica}: {valor}\n"

            return text_context

        except Exception as e:
            raise MetricsStructuringException(f"Erro ao estruturar as métricas: {str(e)}")
