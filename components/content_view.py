#components/content_view.py

from dash import html, dcc

class ContentView:
    """
    Classe responsável pela interface de entrada para a análise CK,
    incluindo os cards de métricas com transição automática e o formulário de entrada.
    """

    def get_metric_cards(self):
        """
        Retorna a lista de métricas a serem exibidas nos cards.

        :return: Lista de dicionários contendo as métricas.
        """
        metrics = [
            {
                'title': 'Coupling between objects',
                'sigla': 'CBO',
                'description': 'Conta o número de dependências que uma classe tem. A ferramenta verifica todos os tipos usados na classe. Ignora dependências do próprio Java.'
            },
            {
                'title': 'Coupling between objects - Modified',
                'sigla': 'CBO-M',
                'description': 'Conta o número de dependências de uma classe, considerando referências que a classe faz e recebe de outras classes.'
            },
            {
                'title': 'Depth Inheritance Tree',
                'sigla': 'DIT',
                'description': 'Conta o número de "pais" que uma classe possui. Todas as classes têm pelo menos DIT 1 (herdando de java.lang.Object).'
            },
            {
                'title': 'Number of Children',
                'sigla': 'NOC',
                'description': 'Conta o número de subclasses imediatas que uma classe possui.'
            },
            {
                'title': 'Number of static invocations',
                'sigla': 'NOSI',
                'description': 'Conta o número de invocações a métodos estáticos que podem ser resolvidas pelo JDT.'
            },
            {
                'title': 'Response for a Class',
                'sigla': 'RFC',
                'description': 'Conta o número de invocações únicas de métodos em uma classe. Pode não lidar corretamente com métodos sobrecarregados.'
            },
            {
                'title': 'Weight Method Class',
                'sigla': 'WMC',
                'description': 'Conta o número de instruções de ramificação em uma classe, também conhecido como complexidade de McCabe.'
            },
            {
                'title': 'Lines of code',
                'sigla': 'LOC',
                'description': 'Conta as linhas de código, ignorando linhas vazias e comentários (Source Lines of Code, SLOC).'
            },
            {
                'title': 'Lack of Cohesion of Methods',
                'sigla': 'LCOM',
                'description': 'Calcula a métrica LCOM. Esta é a primeira versão da métrica e pode não ser confiável.'
            },
            {
                'title': 'Tight Class Cohesion',
                'sigla': 'TCC',
                'description': 'Mede a coesão de uma classe com um valor entre 0 e 1, baseado em conexões diretas entre métodos visíveis.'
            },
            {
                'title': 'Loose Class Cohesion',
                'sigla': 'LCC',
                'description': 'Similar ao TCC, mas também inclui conexões indiretas entre métodos para o cálculo da coesão.'
            }
        ]
        return metrics

    def layout(self):
        """
        Retorna o layout da página de análise CK, incluindo os cards de métricas,
        um texto explicativo e o formulário de entrada para o URL do repositório.

        :return: html.Div com o conteúdo da página.
        """
        # Gera os cards de métricas
        metric_cards = self.get_metric_cards()

        # Cria a estrutura de HTML dos cards
        metric_card_elements = [
            html.Div([
                html.H3(metric['title'], className='metric-title'),
                html.H4(metric['sigla'], className='metric-sigla'),
                html.P(metric['description'], className='metric-description')
            ], className='metric-card') for metric in metric_cards
        ]

        return html.Div([
            # Texto explicativo sobre a ferramenta
            html.Div([
                html.H2("CK Dashboard Analysis", className="content-header"),
                html.P(
                    "Este dashboard utiliza a ferramenta CK para realizar uma análise "
                    "estática de código-fonte em Java. A ferramenta fornece diversas "
                    "métricas de qualidade de código, como acoplamento, coesão e complexidade, "
                    "para ajudar desenvolvedores a identificar possíveis melhorias no código.",
                    className="content-description"
                )
            ], className="intro-container"),

            # Seção de métricas com transição automática
            html.Div(metric_card_elements, className='metrics-container'),

            # Formulário de entrada para a análise CK
            html.Div([
                html.P("Insira o URL do repositório GitHub para análise com a ferramenta CK:"),
                dcc.Input(id='github-url', type='text', placeholder='URL do repositório GitHub', className='url-input'),
                html.Button('Executar Análise', id='execute-button', n_clicks=0, className='execute-button'),
                html.Div(id='output-container')
            ], className='url-input-container')
        ])
