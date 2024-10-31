# Projeto SmartMetric View

Este projeto implementa um dashboard de análise de dados utilizando o framework Dash, baseado em dados de análise estática de códigos Java pela ferramenta CK.

## Estrutura do Projeto

```
projeto_dashboard_ck/
│
├── app.py              # Arquivo principal do Dash, inicializa o app e define o layout global
│
├── assets/             # Diretório para arquivos estáticos como CSS, JS e imagens
│   ├── style.css       # Folha de estilos CSS para personalizar a aparência
│   └── logo.png        # Logotipo da aplicação, se necessário
│
├── components/         # Componentes reutilizáveis da Visão
│   ├── charts.py       # Scripts para criar gráficos com Plotly
│   └── tables.py       # Scripts para gerar tabelas interativas
│
├── controllers/        # Controladores que manipulam a interação entre o Modelo e a Visão
│   ├── callbacks.py    # Callbacks do Dash que respondem a eventos da interface
│   └── router.py       # Roteamento de eventos e chamadas de controle
│
├── models/             # Modelo de dados e lógica de negócio
│   ├── project.py      # Classe para gerenciar informações dos projetos
│   ├── analysis.py     # Classe para gerenciar informações das análises
│   └── metric.py       # Classe para gerenciar as métricas específicas
│
├── services/           # Serviços auxiliares para operações comuns
│   ├── data_loader.py  # Carrega e processa dados da ferramenta CK
│   └── report_generator.py # Gera relatórios com base nas análises
│
├── tests/              # Testes unitários e de integração
│   ├── test_models.py  # Testes para as classes do modelo
│   ├── test_views.py   # Testes para componentes da interface
│   └── test_controllers.py # Testes para a lógica de controle
│
└── requirements.txt    # Dependências do projeto
```
## Descrição dos Componentes Principais

- **app.py**: Este é o ponto de entrada do aplicativo Dash. Ele configura o servidor e define o layout principal do dashboard, conectando todos os componentes e controladores.

- **assets/**: Guarda recursos estáticos como CSS para personalização e imagens. É automaticamente reconhecido pelo Dash, que aplica estilos e imagens conforme necessário.

- **components/**: Contém scripts Python que definem componentes reutilizáveis da interface do usuário, como gráficos e tabelas, que podem ser importados e usados em várias partes do aplicativo.

- **controllers/**: Armazena os controladores que fazem a mediação entre a entrada do usuário (eventos) e a atualização dos modelos e das visualizações. Inclui os callbacks que são cruciais para a interatividade do Dash.

- **models/**: Define as classes Python que encapsulam a lógica de negócio e os dados do aplicativo. Cada classe (Projeto, Análise, Métrica) é responsável por uma parte específica da lógica e dados.

- **services/**: Contém serviços que são usados em várias partes do aplicativo, como carregamento de dados e geração de relatórios, isolando estas funcionalidades para facilitar a manutenção e reutilização.

- **tests/**: Inclui todos os testes unitários e de integração para assegurar que as diferentes partes do aplicativo funcionam corretamente juntas e isoladamente.

- **requirements.txt**: Lista todas as bibliotecas externas necessárias para o projeto, como Dash, Plotly, Pandas, entre outras, que precisam ser instaladas para o aplicativo funcionar.


## Instalação das Dependências

Para garantir que todas as bibliotecas e pacotes necessários para o projeto sejam instalados corretamente, siga os passos abaixo:

1. **Certifique-se de que o Python está instalado**:
   Antes de instalar as dependências, verifique se você tem o Python 3.x instalado em sua máquina. Caso contrário, siga as instruções para instalação no [site oficial do Python](https://www.python.org/downloads/).

2. **Instale as dependências a partir do arquivo `requirements.txt`**:
   Após clonar o repositório ou baixar o projeto, navegue até o diretório principal do projeto no terminal e execute o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

   Esse comando irá instalar todas as bibliotecas listadas no arquivo `requirements.txt`, garantindo que o ambiente esteja configurado corretamente para executar o dashboard.



## Construção da Imagem Docker

Este projeto utiliza uma imagem Docker para encapsular o ambiente de execução necessário para o dashboard, garantindo que ele possa ser executado de forma consistente em qualquer máquina com Docker.

### Pré-requisitos

Antes de construir a imagem Docker, certifique-se de que o Docker está instalado em seu sistema. As instruções para instalação do Docker podem ser encontradas no [site oficial do Docker](https://docs.docker.com/get-docker/).

### Passos para Construção da Imagem

1. **Navegar até o Diretório do Projeto**:
   Abra um terminal e navegue até a pasta _docker_ do projeto SmartMetric View, onde o Dockerfile está localizado.

2. **Construir a Imagem**:
   Execute o seguinte comando no terminal para construir a imagem Docker. Este comando lê o Dockerfile no diretório atual e constrói a imagem.

   ```bash
   docker build -t ck-analyzer .
   ```

   Este comando executa as instruções definidas no Dockerfile, que incluem baixar a imagem base, instalar as dependências necessárias, copiar os arquivos do projeto para dentro da imagem e configurar o ambiente de execução.

3. **Verificar a Imagem**:
   Após a construção ser completada, você pode verificar se a imagem foi criada com sucesso listando todas as imagens Docker disponíveis:

   ```bash
   docker images
   ```

   Procure por `ck-analyzer` na lista para confirmar que a imagem está pronta para uso.

### Utilização da Imagem

A imagem Docker construída está pronta para ser usada para iniciar o servidor do dashboard Dash. As instruções de execução da imagem Docker são parte do sistema de implantação e não são necessárias para o processo de construção.


