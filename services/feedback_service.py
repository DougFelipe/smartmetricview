# services/feedback_service.py
import os

class FeedbackService:
    def __init__(self):
        self.feedback_dir = os.path.join(os.getcwd(), 'feedback')

        # Certifica-se de que o diretório de feedbacks existe
        if not os.path.exists(self.feedback_dir):
            os.makedirs(self.feedback_dir)

    def submit_feedback(self, username, feedback):
        try:
            # Validação básica
            if not username:
                username = "Anônimo"

            # Gravar o feedback em um arquivo simples
            feedback_file = os.path.join(self.feedback_dir, f"{username}_feedback.txt")
            with open(feedback_file, 'a') as f:
                f.write(f"{feedback}\n\n")

            return "Obrigado pelo seu feedback!"
        except Exception as e:
            return f"Erro ao salvar feedback: {str(e)}"
