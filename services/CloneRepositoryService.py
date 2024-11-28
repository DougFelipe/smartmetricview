import subprocess
import os
import shutil
from exceptions.RepositoryCloneException import RepositoryCloneException

class CloneRepositoryService:

    def clone_repository(self, repo_url):
        # Define o diretório para clonar o repositório
        base_directory = os.path.join(os.getcwd(), "cloned_repos")
        if not os.path.exists(base_directory):
            os.makedirs(base_directory)

        repo_name = repo_url.split('/')[-1].replace('.git', '')
        repo_path = os.path.join(base_directory, repo_name)

        if os.path.exists(repo_path):
            shutil.rmtree(repo_path)

        try:
            subprocess.check_output(["git", "clone", repo_url, repo_path])
            return repo_path
        except subprocess.CalledProcessError as e:
            raise RepositoryCloneException(f"Erro ao clonar o repositório: {e.output.decode('utf-8')}")
        except Exception as e:
            raise RepositoryCloneException(f"Erro inesperado: {str(e)}")
