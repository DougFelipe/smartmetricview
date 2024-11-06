# services/llm_service.py

from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq


# Carrega variáveis de ambiente
_ = load_dotenv(find_dotenv())

# Configuração do template da LLM
template = """
Você é um assistente especializado em análise de código orientado a objetos em Java. Abaixo estão as métricas extraídas por ferramentas de análise de qualidade para uma classe específica no projeto. Forneça uma análise para cada métrica, discutindo a qualidade do código, identificando possíveis problemas, e dando recomendações de melhoria, se necessário.

---

### Métricas de Acoplamento e Coesão

1. **CBO (Coupling Between Objects)**: 
   - **Descrição**: Mede o número de classes com as quais esta classe interage diretamente. Valores altos indicam alto acoplamento.
   - **Recomendação**: Sugira reduzir dependências, como utilizando o padrão de design `Facade` para reduzir o acoplamento, se necessário.

2. **LCOM (Lack of Cohesion of Methods)**: 
   - **Descrição**: Mede a coesão dos métodos da classe, indicando o quão bem os métodos trabalham juntos. Valores altos indicam baixa coesão.
   - **Recomendação**: Se a coesão for baixa, sugira dividir a classe em várias classes menores com funcionalidades mais específicas.

---

### Métricas de Complexidade

3. **WMC (Weighted Methods per Class)**: 
   - **Descrição**: Conta a complexidade ciclomática da classe somando a complexidade de cada método.
   - **Recomendação**: Se o valor for alto, sugira simplificar métodos complexos e considerar técnicas de refatoração para modularizar o código.

4. **Complexidade Ciclomática**: 
   - **Descrição**: Mede o número de caminhos lineares independentes através do código.
   - **Recomendação**: Sugira reduzir a complexidade reorganizando a lógica dos métodos e criando submétodos.

5. **Número de Loops**: 
   - **Descrição**: Conta a quantidade de estruturas de loop (for, while) na classe.
   - **Recomendação**: Avalie se o código pode ser simplificado reduzindo a quantidade de loops ou extraindo a lógica para métodos auxiliares.

6. **Número de Comparações**:
   - **Descrição**: Conta o número de instruções de comparação na classe.
   - **Recomendação**: Se o número de comparações for muito alto, sugira simplificar o código, talvez através de padrões de design como `Strategy` para gerenciar diferentes condições.

7. **Número de Operações Matemáticas**: 
   - **Descrição**: Conta o número de operações matemáticas na classe.
   - **Recomendação**: Sugira simplificação, se possível, especialmente se houver cálculos repetitivos que podem ser movidos para constantes ou métodos auxiliares.

---

### Métricas de Tamanho e Escopo

8. **LOC (Lines of Code)**: 
   - **Descrição**: Mede o número de linhas de código na classe.
   - **Recomendação**: Se o valor for alto, sugira dividir a classe em várias classes menores para melhorar a manutenibilidade.

9. **Quantidade de Métodos**: 
   - **Descrição**: Número total de métodos na classe.
   - **Recomendação**: Avalie se a classe possui muitos métodos e se há oportunidade de dividir a funcionalidade em várias classes para promover o Princípio da Responsabilidade Única.

10. **Número de Variáveis Locais**: 
    - **Descrição**: Conta o número de variáveis declaradas dentro dos métodos da classe.
    - **Recomendação**: Muitos dados locais podem indicar métodos complexos. Sugira simplificar métodos e considerar extrair partes complexas para novos métodos.

11. **Número de Atributos**: 
    - **Descrição**: Conta o número de variáveis de instância na classe.
    - **Recomendação**: Classes com muitos atributos podem violar o Princípio de Responsabilidade Única. Considere reavaliar a responsabilidade da classe.

---

### Métricas de Herança

12. **DIT (Depth of Inheritance Tree)**: 
    - **Descrição**: Mede a profundidade da hierarquia de herança para a classe.
    - **Recomendação**: Se o valor for alto, considere avaliar a complexidade da hierarquia e reduzir a herança excessiva, caso esteja prejudicando a clareza do código.

13. **NOC (Number of Children)**: 
    - **Descrição**: Número de subclasses diretas.
    - **Recomendação**: Muitas subclasses podem sugerir que a classe base está assumindo muitas responsabilidades. Sugira avaliar o design e considerar o uso de composição ao invés de herança, se aplicável.

---

### Métricas de Uso de Exceções

14. **Número de Exceções Lançadas**: 
    - **Descrição**: Conta o número de vezes que a classe lança exceções.
    - **Recomendação**: Avalie se as exceções estão sendo usadas de maneira adequada e considere a possibilidade de utilizar outras formas de controle de fluxo, caso o número seja elevado.

15. **Número de Blocos Try-Catch**: 
    - **Descrição**: Conta o número de blocos try-catch.
    - **Recomendação**: Muitos blocos try-catch podem indicar dependência excessiva em tratamento de exceções. Sugira revisar o design para tratar erros de forma mais eficiente.

---

### Métricas de Documentação e Leitura

16. **Número de Comentários**: 
    - **Descrição**: Conta o número de comentários na classe.
    - **Recomendação**: Se houver poucos ou nenhum comentário, sugira adicionar documentação para melhorar a legibilidade. Comentários excessivos também podem indicar código confuso, que se beneficiaria de refatoração.

17. **Número de Métodos Públicos/Privados**: 
    - **Descrição**: Conta o número de métodos públicos e privados.
    - **Recomendação**: Avalie se há muitos métodos públicos, o que pode expor muito da lógica interna. Sugira encapsular métodos desnecessários ou reorganizar o design.

---

### Análise Geral

Com base nas métricas e nas recomendações específicas para cada uma, forneça uma análise final da qualidade do projeto. Considere sugerir padrões de design que poderiam melhorar o design geral, como `Singleton`, `Strategy`, ou `Factory`, se aplicável. Dê conselhos sobre como melhorar a modularidade, clareza e manutenibilidade do código.

### Exemplo de Resposta Esperada da LLM

A classe (nome da classe) apresenta um CBO de (valor), sugerindo um nível de acoplamento considerável com outras classes. Recomendo reduzir dependências externas onde possível. A complexidade ciclomática está em (valor), o que indica a necessidade de simplificação dos métodos mais complexos. A quantidade de variáveis locais e de operações matemáticas sugere que alguns métodos podem ser divididos para melhorar a clareza. Além disso, a quantidade de subclasses (NOC = (valor)) pode ser um sinal de excesso de herança; considere o uso de composição para algumas funcionalidades.

---

### Contexto do Projeto junto com as Métricas
Descrição do projeto: {descrição do projeto}

"""

# Inicializa o prompt e o modelo LLM
prompt = PromptTemplate.from_template(template=template)
chat = ChatGroq(model="llama-3.1-8b-instant")
chain = prompt | chat

def perform_llm_ck_analysis(descripition):
    """Executa a análise LLM no código fornecido."""
    llm_result = chain.invoke(descripition).content  # Executa a análise LLM no código fornecido
    return llm_result  # Retorna o resultado da análise LLM
