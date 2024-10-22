from dash import html, dcc

class FeedbackView:
    """
    Classe responsável pela interface de feedback do usuário.
    """

    def layout(self):
        """
        Retorna o layout da página de feedback.
        
        :return: html.Div com o formulário de feedback.
        """
        return html.Div([
            html.Div([
                html.H3("Deixe seu Feedback", className="feedback-title"),

                # Nome do Usuário
                dcc.Input(
                    id='username',
                    type='text',
                    placeholder='Seu Nome',
                    value='',
                    className='feedback-input'
                ),

                # E-mail do Usuário
                dcc.Input(
                    id='user-email',
                    type='email',
                    placeholder='Seu E-mail (opcional)',
                    value='',
                    className='feedback-input'
                ),

                # Assunto
                dcc.Dropdown(
                    id='feedback-subject',
                    options=[
                        {'label': 'Problema Técnico', 'value': 'Problema Técnico'},
                        {'label': 'Sugestão de Melhoria', 'value': 'Sugestão de Melhoria'},
                        {'label': 'Dúvida ou Pergunta', 'value': 'Dúvida ou Pergunta'},
                        {'label': 'Outro', 'value': 'Outro'}
                    ],
                    placeholder='Escolha um assunto',
                    className='feedback-dropdown'
                ),

                # Descrição do Feedback
                dcc.Textarea(
                    id='user-feedback',
                    placeholder='Escreva seu feedback aqui...',
                    style={'width': '100%', 'height': 150},
                    value='',
                    className='feedback-textarea'
                ),

                # Satisfação Geral (alterado para RadioItems)
                html.Label("Avalie sua satisfação geral:", className='feedback-label'),
                dcc.RadioItems(
                    id='satisfaction-rating',
                    options=[
                        {'label': '1 - Muito Insatisfeito', 'value': 1},
                        {'label': '2 - Insatisfeito', 'value': 2},
                        {'label': '3 - Neutro', 'value': 3},
                        {'label': '4 - Satisfeito', 'value': 4},
                        {'label': '5 - Muito Satisfeito', 'value': 5},
                    ],
                    value=3,  # Valor padrão
                    className='feedback-radio-items',
                    labelStyle={'display': 'block'}
                ),

                # Deseja ser contatado?
                dcc.Checklist(
                    id='contact-permission',
                    options=[{'label': 'Deseja ser contatado sobre este feedback?', 'value': 'contact'}],
                    value=[],
                    className='feedback-checklist'
                ),

                # Preferência de Contato
                dcc.Dropdown(
                    id='contact-preference',
                    options=[
                        {'label': 'E-mail', 'value': 'E-mail'},
                        {'label': 'Telefone', 'value': 'Telefone'}
                    ],
                    placeholder='Preferência de Contato',
                    className='feedback-dropdown',
                    style={'display': 'none'}  # Por padrão, escondido até o usuário marcar o checkbox
                ),

                # Botão de Enviar
                html.Button('Enviar Feedback', id='send-feedback', n_clicks=0, className='feedback-button'),

                # Resposta do Feedback
                html.Div(id='feedback-response', className='feedback-response')
            ], className='feedback-card')
        ])
