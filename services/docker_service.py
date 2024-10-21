# services/docker_service.py

import subprocess
import os

def run_ck_analysis(repo_url):
    """
    Executa a ferramenta CK em um repositório GitHub via Docker.
    
    :param repo_url: URL do repositório GitHub.
    :return: Saída do comando Docker ou mensagem de erro.
    """
    current_directory = os.getcwd()
    output_directory = os.path.join(current_directory, "output")

    try:
        result = subprocess.check_output(
            [
                'docker', 'run',
                '-e', f'REPO_URL={repo_url}',
                '-v', f"{output_directory}:/app/output",
                'ck-analyzer'
            ],
            stderr=subprocess.STDOUT
        )
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Erro durante a execução: {e.output.decode("utf-8")}'
