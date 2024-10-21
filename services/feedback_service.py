# services/feedback_service.py
import os

class FeedbackService:
    """
    Serviço responsável por armazenar o feedback do usuário.
    """

    def __init__(self):
        self.feedback_dir = os.path.join(os.getcwd(), 'feedback')

        # Certifica-se de que o diretório de feedback existe
        if not os.path.exists(self.feedback_dir):
            os.makedirs(self.feedback_dir)

    def submit_feedback(self, username, feedback):
        """
        Processa e salva o feedback do usuário em um arquivo de texto.
        
        :param username: Nome do usuário que enviou o feedback.
        :param feedback: Conteúdo do feedback enviado.
        :return: Mensagem de sucesso ou erro.
        """
        try:
            if not username:
                username = "Anônimo"

            feedback_file = os.path.join(self.feedback_dir, f"{username}_feedback.txt")
            with open(feedback_file, 'a') as f:
                f.write(f"{feedback}\n\n")

            return "Obrigado pelo seu feedback!"
        except Exception as e:
            return f"Erro ao salvar feedback: {str(e)}"
