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

