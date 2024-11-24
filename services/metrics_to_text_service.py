class MetricsToTextConvert:
    def metrics_to_text_convert(self, description_project, outputclass, outputfield, outputmethod, outputvariable):
        # Descrição inicial do projeto
        text_context = f"Descrição do Projeto: {description_project}\n\n\n"

        # Adiciona as métricas por classe
        text_context += "Métricas das Classes:\n"
        for classe, metrics in outputclass.items():
            text_context += f"\nClasse: {classe}\n"
            for metrica, valor in metrics.items():
                if metrica != 'class':  # Exclui a coluna 'class'
                    text_context += f"  {metrica}: {valor}\n"

        # Adiciona as métricas dos campos (fields)
        text_context += "\nMétricas dos Campos (Fields):\n"
        for classe, metrics in outputfield.items():
            text_context += f"\nClasse: {classe}\n"
            for metrica, valor in metrics.items():
                if metrica != 'class':
                    text_context += f"  {metrica}: {valor}\n"

        # Adiciona as métricas dos métodos (methods)
        text_context += "\nMétricas dos Métodos (Methods):\n"
        for classe, metrics in outputmethod.items():
            text_context += f"\nClasse: {classe}\n"
            for metrica, valor in metrics.items():
                if metrica != 'class':
                    text_context += f"  {metrica}: {valor}\n"

        # Adiciona as métricas das variáveis (variables)
        text_context += "\nMétricas das Variáveis (Variables):\n"
        for classe, metrics in outputvariable.items():
            text_context += f"\nClasse: {classe}\n"
            for metrica, valor in metrics.items():
                if metrica != 'class':
                    text_context += f"  {metrica}: {valor}\n"

        return text_context