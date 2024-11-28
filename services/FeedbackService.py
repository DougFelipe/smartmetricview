# services/FeedbackService.py
import os
from exceptions.FeedbackSubmissionException import FeedbackSubmissionException


class FeedbackService:
    def __init__(self):
        self.feedback_dir = os.path.join(os.getcwd(), 'feedback')

        if not os.path.exists(self.feedback_dir):
            os.makedirs(self.feedback_dir)

    def submit_feedback(self, username, feedback):
        try:
            if not username:
                username = "Anônimo"

            # Gravar o feedback em um arquivo simples
            feedback_file = os.path.join(self.feedback_dir, f"{username}_feedback.txt")
            with open(feedback_file, 'a') as f:
                f.write(f"{feedback}\n\n")

            return "Obrigado pelo seu feedback!"

        except FileNotFoundError as e:
            raise FeedbackSubmissionException(f"Erro ao acessar o diretório para salvar o feedback: {str(e)}")

        except PermissionError as e:
            raise FeedbackSubmissionException(f"Erro de permissão ao tentar salvar o feedback: {str(e)}")

        except Exception as e:
            raise FeedbackSubmissionException(f"Erro desconhecido ao salvar feedback: {str(e)}")
