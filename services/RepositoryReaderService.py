import os

class RepositoryReaderService:
    """Classe responsável por ler o código de um repositório clonado."""

    @staticmethod
    def read_code(repo_path, extension=".java"):
        code = ""
        for root, _, files in os.walk(repo_path):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        code += f.read() + "\n\n"
        return code
