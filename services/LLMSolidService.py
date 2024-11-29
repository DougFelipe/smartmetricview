# services/llm_service.py

from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq


# Carrega variáveis de ambiente
_ = load_dotenv(find_dotenv())

# Configuração do template da LLM
template = """
Você é um analista de código Java especializado em padrões de design e boas práticas de desenvolvimento. Sua tarefa é analisar o código fornecido e sugerir melhorias para que ele siga os princípios SOLID.

Abaixo está o código Java para análise:

{text}

**Saída esperada:**
- **Análise detalhada**: Comentários sobre qualquer violação dos princípios SOLID.
- **Sugestões específicas de melhoria**: Código exemplificado com explicações de como aplicar o princípio SOLID.
"""

# Inicializa o prompt e o modelo LLM
prompt = PromptTemplate.from_template(template=template)
chat = ChatGroq(model="llama-3.1-8b-instant")
chain = prompt | chat

class LLMSolidService:
    def perform_llm_analysis(self, code):
        """Executa a análise LLM com base nos padrões SOLID com o código fornecido."""
        try:
            llm_result = chain.invoke(code).content
            return llm_result
        except Exception as e:
            raise Exception(f"Erro ao realizar a análise LLM: {str(e)}")
